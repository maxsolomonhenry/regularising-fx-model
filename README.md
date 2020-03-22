# regularising-fx-model

An investigation into the effects of weight regularisation on the modelling capability of the CAFx model created by Martínez Ramírez M. A., Benetos, E. and Reiss J. D.

## Dependancies

A CUDA enabled system.

### Python libraries

``` Python
numpy==1.16.1
scipy==1.2.0
sacred==0.7.4
keras==2.2.4
tensorflow-gpu==1.14
h5py
sklearn
brian2
brian2hears
```

## Usage

``` Python
python ./main.py with model_type='CAFx'
python ./main.py with model_type='CAFxR'
```

## Dataset

The data used to train, evaluate and test the models was created as part of [DL-AFx](https://github.com/mchijmma/DL-AFx/tree/master/src) by Martínez et al. [1]. With the original clean guitar and bass signals created by Stein et al. [2]

[1] Martínez Ramírez M. A., Benetos, E. and Reiss J. D., “Deep Learning for Black-Box Modeling of Audio Effects” Applied Sciences 10, no. 2, p.638, January 2020.

[2] Stein, M.; Abeßer, J.; Dittmar, C.; Schuller, G. Automatic detection of audio effects in guitar and bass recordings. In Proceedings of the 128th Audio Engineering Society Convention, London, UK, 22–25 May 2010.