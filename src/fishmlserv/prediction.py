import fire
from sklearn.neighbors import KNeighborsClassifier
from fishmlserv.model.manager import get_model_path
import pickle

def prediction(length: float, weight: float):
    """
    length와 weight를 이용한 물고기 예측 모델 (빙어, 도미)
OCI runtime exec failed: exec failed: unable to start container process: exec: "prediction": executable file not found in $PATH: unknown
    Args:
        length: 물고기의 길이(float)
        weight: 물고기의 무게(float)

    Return:
        예측된 물고기의 종류
    """
    model_path=get_model_path()
    with open(model_path, 'rb') as f:
        fish_model=pickle.load(f)
    
    result = fish_model.predict([[length, weight]])
    
    if result[0] == 1:
        fish = '도미'
    else:
        fish = '빙어'
    
    print(fish)
    return fish


def main():
    fire.Fire(prediction)

