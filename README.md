# Trening-i-porównanie-dwóch-model-w-YOLO
## Cel projektu
Stworzenie dwóch modeli YOLO (yolov8n oraz yolo11n) do rozpoznawania pojazdów na zajęciach z drona oraz porównanie obu modeli biorąc pod uwagę ich hiperparametry.

## Zbiór danych i trening
Do treningu został wykorzystany zbiór **VisDrone** (podzbiór 20% danych). Zawiera on zdjęcia różnych pojazdów, pieszych, chodnika z lotu z lotu ptaka, obiekty są małe, pod różnymi kątami oraz oświetleniem.
Oba modele były trenowane na 10 epokach.

## Porównanie modeli z dokumentacji Ultralytics
### YOLOv8n:

<img width="867" height="141" alt="obraz" src="https://github.com/user-attachments/assets/df76eaca-a871-42b8-be63-9b02c425f512" />

- mniejsza dokładność
- wysoki FPS

### YOLO11n:

<img width="871" height="139" alt="obraz" src="https://github.com/user-attachments/assets/4c8f9bb3-fdfc-450f-bcff-add3ee980f02" />

- większa dokładność
- mniejszy FPS

## Porównanie modeli na własnych danych uzyskanych podczas treningu
| Metryka | YOLOv8n | YOLO11n |
| :--- | :---: | :---: |
| Precision | 0.355 | 0.348 |
| Recall | 0.258 | 0.264 |
| mAP@0.5 | 0.228 | 0.230 |
| mAP@0.5:0.95 | 0.122 | 0.124 |
