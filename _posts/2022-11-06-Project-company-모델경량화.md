---
layout: post
title: "edge computing 기반 DL 모델 경량화 & serving"
subtitle: "Pruning, Quantization, TensorRT를 활용한 실시간 추론 시스템 설계"
categories: Project
tags: Company
comments: true
---

### 제조 환경에서 실시간 추론이 가능한 

### AI 모델 경량화 및 서빙 방법을 탐색한 실험 기반 프로젝트입니다.

<br/>

### 1. 프로젝트 개요

- Member : 김경록 외 1명
- Status : Complete
- 사용언어 : Python, Shell
- 핵심 기술 : PyTorch, TensorRT, ONNX, Flask, NVIDIA Triton, Docker
- 대상 디바이스 : Jetson Nano, x86 Desktop

<br/>

### 2. Why 

- 왜 Edge + 경량화가 중요한가?

  - 전통적인 AI 모델 서빙은 중앙 집중형 서버(클라우드) 구조를 기반으로 합니다.
  - 그러나 제조 환경에서는 네트워크 지연이나 불안정성으로 인해 AI 추론 응답 시간 요구를 충족하지 못할 수 있습니다.
  - 특히 Edge Device(예: 센서, IoT 기기 등)가 늘어날수록 네트워크 병목 발생 가능성이 높아집니다.

> 따라서, **Edge 단에서 직접 추론이 가능한 경량화된 모델 + 서빙 구조**의 필요성이 대두됩니다.

<br/>

### 3. 문제 정의

- Edge Device(예: Jetson Nano)는 리소스(메모리/연산 능력)가 매우 제한됨  
- 경량화 없이 일반 AI 모델을 배포할 경우 추론 속도 저하, 과부하 발생  
- 다양한 논문 기반 모델 압축 기법은 실험 조건이 달라 Base Line으로 사용이 어려움

<br/>

### 4. 실험 설계 및 아키텍처

#### (a) 실험 대상 및 구성 요소

- **디바이스**: Nvidia Jetson Nano, x86 Desktop
- **모델**: ResNet, MobileNet, EfficientNet(b0, b7)  (TorchHub 기반)
- **압축 방식**: Pruning, Quantization, ONNX 변환, TensorRT 최적화
- **서빙 방식**: Flask API, NVIDIA Triton Inference Server

#### (b) 실험 아키텍처

- Server Process (Jetson 내부 혹은 Docker 컨테이너 기반)
- Client Process (이미지 전송 및 추론 결과 수신)
- Monitor Process (리소스 사용량 및 응답시간 측정)

```text
[Client] → [Server (Flask/Triton)] → [Optimized DL Model]
```

<br/>

### 5. 실험 결과 요약 및 인사이트

Lesson Learned

    TensorRT 최적화는 실질적인 추론 속도 향상에 매우 효과적임.

    다만, TensorRT는 Nvidia 계열 디바이스에서만 사용 가능하며, 실제 사용 디바이스에서 변환을 수행해야 효과가 최대화됨

    Pruning & Quantization은 메모리 사용량을 크게 줄일 수 있으나, 
    
    정확도 저하가 발생할 수 있어 모델에 따라 선택적 적용이 필요

    + Jetson Nano의 경우 fp16으로 경량화를 시도 하였지만

    실질적인 적용이 int8만 사용이 되었기에

    Computing 자원 자체의 문제도 고려하여서 적용 필요.