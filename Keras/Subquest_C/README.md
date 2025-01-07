# CIFAR-10 분류를 위한 ResNet-50과 Keras Tuner 활용

## 프로젝트 개요

이 프로젝트는 CIFAR-10 데이터셋을 분류하기 위해 ResNet-50 모델을 활용하고, Keras Tuner를 이용해 최적의 하이퍼파라미터를 찾는 실험 과정과 결과를 정리한 것입니다.

---

## 실습 내용

### 1. 라이브러리 임포트

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.optimizers import Adam, RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras_tuner import RandomSearch
```

### 2. 데이터셋

#### 데이터셋 로드 및 전처리

- CIFAR-10 데이터셋은 10개의 클래스로 이루어진 이미지 분류 데이터셋입니다.

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # 정규화
y_train, y_test = y_train.flatten(), y_test.flatten()  # (N, 1) -> (N,)
```

#### 데이터 증강

- 데이터 증강을 통해 모델의 일반화 성능을 향상시킵니다.

```python
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
datagen.fit(x_train)
```

---

### 3. 모델 구성

#### ResNet-50 기반 모델 빌더 함수

- ResNet-50을 Backbone으로 사용하며, Keras Tuner로 튜닝 가능한 하이퍼파라미터를 포함한 Fully Connected Layer를 추가했습니다.

```python
def build_model(hp):
    base_model = ResNet50(
        weights='imagenet',
        include_top=False,  # 최상위 Fully Connected Layer 제외
        input_shape=(32, 32, 3)
    )
    base_model.trainable = False  # 사전 학습된 레이어 고정

    inputs = layers.Input(shape=(32, 32, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(
        units=hp.Choice('dense_units', values=[128, 256, 512]),
        activation='relu'
    )(x)
    x = layers.Dropout(rate=hp.Float('dropout_rate', min_value=0.2, max_value=0.5, step=0.1))(x)
    outputs = layers.Dense(10, activation='softmax')(x)

    model = models.Model(inputs, outputs)
    model.compile(
        optimizer=hp.Choice('optimizer', values=['adam', 'rmsprop']),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model
```

---

### 4. 하이퍼파라미터 튜닝

#### Keras Tuner 초기화

- 최적의 하이퍼파라미터를 탐색하기 위해 RandomSearch를 사용합니다.

```python
tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=10,
    executions_per_trial=2,
    directory='resnet50_tuning',
    project_name='cifar10'
)
```

#### 콜백 정의

- EarlyStopping과 ReduceLROnPlateau를 활용해 학습 과정에서 과적합을 방지하고 학습률을 동적으로 조정합니다.

```python
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2)
```

#### 하이퍼파라미터 탐색

```python
tuner.search(
    datagen.flow(x_train, y_train, batch_size=64),
    epochs=20,
    validation_data=(x_test, y_test),
    callbacks=[early_stopping, reduce_lr]
)

# 최적의 하이퍼파라미터 출력
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(f"Best dense_units: {best_hps.get('dense_units')}")
print(f"Best dropout_rate: {best_hps.get('dropout_rate')}")
print(f"Best optimizer: {best_hps.get('optimizer')}")
```

---

### 5. 최적의 모델 학습 및 평가

#### 최적의 모델 구성 및 학습

```python
model = tuner.hypermodel.build(best_hps)

history = model.fit(
    datagen.flow(x_train, y_train, batch_size=64),
    epochs=50,
    validation_data=(x_test, y_test),
    callbacks=[early_stopping, reduce_lr]
)
```

#### 검증 데이터 평가

```python
val_loss, val_accuracy = model.evaluate(x_test, y_test)
print(f"Validation Loss: {val_loss}")
print(f"Validation Accuracy: {val_accuracy}")
```

---

## 실험 결과

- **Best Hyperparameters:**

  - `dense_units`:
  - `dropout_rate`:
  - `optimizer`:

- **Validation Metrics:**
  - `Validation Loss`:
  - `Validation Accuracy`:

---

## 결론

Keras Tuner를 활용해 ResNet-50 기반의 모델에서 최적의 하이퍼파라미터를 찾으려고 하였으나 제한 시간 안에 테스트를 완료하지 못했습니다. 더불어 데이터 증강과 튜닝을 통해 CIFAR-10 데이터셋에서 높은 검증 정확도를 달성하려고 하였으나 이 또한 여러 번의 시도를 통해 개선하려고 하는 과정에서 시간 제한으로 인해 최종적으로 ResNet을 사용하지 않고 Keras Tuner를 사용하지 않고 사전 학습된 CNN 모델을 이용해도 87%의 정확도가 나오는데 그것보다는 높아야 Keras Tuner를 사용하는 의미가 있지 않겠는가 하는 생각 때문에 여러가지 시도해보다가 제한시간을 맞추지 못했습니다. 하지만 일단 시도했던 코드는 첨부하도록 하겠습니다.
