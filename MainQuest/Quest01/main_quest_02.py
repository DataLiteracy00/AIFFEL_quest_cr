import random

def get_attack_power(offense):
  return random.randint(1, offense)

class Character:
  # Q1.이름, 레벨, 체력, 공격력, 방어력의 속성을 가짐
  def __init__(self, name, level, health, offense, defense):
    self.name = name
    self.level = level
    self.health = health
    self.offense = offense
    self.defense = defense

  # Q1.인스턴스의 현재 체력이 0 이상인지 bool 값을 반환하는 is_alive 메서드 만들기
  def is_alive(self):
    return True if self.health >= 0 else False

  # Q1.공격을 받았을 때, (받은 데미지 - 본인의 방어력)만큼 현재 체력이 감소하는 take_damage 메서드 만들기
  def take_damage(self,attack):
    if self.defense > attack:
      return
    else:
      self.health -= attack
  
  # Q1.타겟에게 데미지를 입히는 attack_target 메서드 만들기
  def attack_target(self, attack):
    attack = get_attack_power(self.offense + 1)
    return attack

# Q2.Character 상속 받기
class Player(Character):
  # Q2.레벨 1, 체력 100, 공격력 25, 방어력 5로 초기화하기
  def __init__(self, name, level = 1, health = 100, offense = 25, defense = 5, experience = 0):
    super().__init__(name, level, health, offense, defense)
    self.experience = experience

  # Q2.인수로 받은 정수 만큼 경험치를 획득하는 gain_experience 메서드 만들기
  def gain_experience(self, exp):
    self.experience += exp

  # Q2.현재 경험치가 50이상이면 레벨을 1, 공격력을 10, 방어력을 5씩 올리는 level_up 메서드 만들기
  def level_up(self):
    if self.experience >= 50:
      self.level += 1
      self.offense += 10
      self.defense += 5
      self.experience -= 50

      print()
      print("-------------------------")
      print("레벨업!, 레벨 : ", self.level)
      print("-------------------------")
      print()

def get_random_num(start_num, end_num):
  return random.randint(start_num, end_num)
  
# Q2.Character를 상속 받기
class Monster(Character):
  # Q2.몬스터의 레벨에 비례하는 체력, 공격력, 방어력 초기화하기
  def __init__(self, name, level):
    health = get_random_num(10, 31) * level
    offense = get_random_num(5, 21) * level
    defense = get_random_num(1, 6) * level
    super().__init__(name, level, health, offense, defense)

# Q3.battle 함수
def battle(player, monster):
  # Q3.Player 인스턴스와  Monster 인스턴스를 인수로 받아 둘 중 하나의 체력이 0 이하가 될 때까지 공격을 주고 받는 함수
  while player.health >= 0 and monster.health >= 0:
    player_attack = player.attack_target(player.offense)
    monster.take_damage(player_attack)
    monster_attack = monster.attack_target(monster.offense)
    player.take_damage(monster_attack)

    print(f"{player.name}의 체력 : {player.health}")
    print(f"{monster.name}의 체력 : {monster.health}")
  
  # Q3.만약 Player 인스턴스가 살아남았다면 
  if player.health > 0:
    player.gain_experience(monster.level * 20)
    player.level_up()
    print("전투 승리")
  # Q3.Player 인스턴스가 살아남지 못했을 경우
  else:
    print("전투 패배..")

def main():
  # Q3.몬스터의 이름, 레벨이 매핑된 딕셔너리 정의하기
  monster_dict = {'슬라임': 1, '고블린': 2, '오크': 3}

  # Q3.사용자로부터 이름을 입력받아 Player 인스턴스 생성하기
  player_name = input("Player 이름을 입력해서 캐릭터를 생성해주세요 : ")
  player = Player(player_name)
  
  # Q3. 몬스터 딕셔너리로부터 Monster 인스턴스 동적으로 생성하여 리스트에 저장
  monsters = [Monster(name, level) for name, level in monster_dict.items()]
  
  # Q3.생성된 Monster 인스턴스와 Player 인스턴스가 battle 함수를 통해 전투
  for monster in monsters:
    print(f"\n{monster.name}와 전투를 시작합니다!")
    battle(player, monster)

    if player.health <= 0:
      print("게임오버")
      return

main()