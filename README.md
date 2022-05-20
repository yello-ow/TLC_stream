<div align="center">
  <h1> Kafka, Flink를 이용한 택시요금 예측 Project </h1>
  택시요금 예측을 위한 실시간 데이터 처리 스트림 파이프라인 구축 
  <br><br>
  <img src="https://user-images.githubusercontent.com/86868063/169539953-c84b5f1c-781d-4582-a17e-8366b604e502.png">

  <br><br>
  
  ### ⚒ 기술 스택
  ![Python](https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=FFFFFF) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=FFFFFF) ![sckit_learn](https://img.shields.io/badge/scikt_learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=FFFFFF) ![Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=Apache+Kafka&logoColor=FFFFFF) ![Flink](https://img.shields.io/badge/Apache_Flink-E6526F?style=flat-square&logo=Apache+Flink&logoColor=FFFFFF) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=FFFFFF) 
  <br><br>
  
</div>

## 프로젝트 개요 
- 📅 프로젝트 기간: 2022.04.18 - 2022.04.29
<br>

## 프로젝트 목표
- 대용량 데이터에서의 파이프라인을 구축
- TLC 데이터를 이용해 택시요금 예측 ML 모델링 
- 실시간 데이터 처리 스트림 파이프라인 구축 
<br>

## 데이터 파이프라인 
<img src="https://user-images.githubusercontent.com/86868063/169541380-764a1b00-c4d6-49ef-b3cd-b6fdd657e32f.png">
<br>

## 프로젝트 과정
- Pandas를 이용해 데이터 전처리 
- scikit-learn을 이용해 전처리 완료된 데이터로 머신러닝 모델 학습
- Kafka Producer를 이용해 데이터를 실시간으로 전송 
- Kafka에서 전송받은 데이터를 Flink를 이용해 머신러닝 모델에 넣고 실시간으로 예측값 출력 
<br>

## 프로젝트 회고
- 이번 프로젝트는 사실 이전에 spark와 airflow를 이용한 데이터 파이프라인 프로젝트를 보완하기 위해 시작한 프로젝트였는데 여전히 spark에서 학습한 모델을 flink에서 실시간 데이터에 적용하는데 어려움을 느껴 spark, airflow, kafka, flink 모두를 사용하는 것은 포기하고 이전에 사용해보지 않은 kafka, flink 위주의 프로젝트를 진행했다. 
- spark sql과 spark mllib 대신 익숙한 pandas와 scikit-learn을 이용했지만 flink에서 복잡한 모델은 사용할 수가 없어 모델의 성능이 좋지 못한 점은 매우 아쉽다.  하지만 이번 프로젝트의 목적이 실시간 데이터 처리 스트림 파이프라인 구축인 만큼 나름 파이프라인 단계 구성은 나쁘지 않다고 생각한다. 
- 파이프라인에는 flink에서 예측한 결과값을 저장한다고 되어있지만 대용량 data가 실시간으로 들어오기 떄문에 비용, 용량 문제로 클라우드나 local 환경에 저장 할 수 없었다. 실제 업무에서는 예측한 결과값으로 서비스를 제공하기 때문에 이 부분은 실제 업무에 적용된다면 보완 가능하다고 생각한다. 
- 추후에는 spark, airflow, kafka, flink를 모두 사용하는 프로젝트를 완벽하게 완성해보고 싶다는 욕심이 든다. 
<br>
