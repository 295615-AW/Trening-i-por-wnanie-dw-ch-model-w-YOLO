# Trening-i-porównanie-dwóch-model-w-YOLO
Stworzenie dwóch modeli YOLO - yolov8n oraz yolo11n, do rozpoznawania pojazdów na zajęciach. Porównanie obu modeli.

## Zbiór danych
VisDrone - zawiera zdjęcia róznych pojazdów, chodnika i pieszych z lotu drona

## Modele
YOLOv8n:

<img width="867" height="141" alt="obraz" src="https://github.com/user-attachments/assets/df76eaca-a871-42b8-be63-9b02c425f512" />

- mniejsza dokładność
- większy klatkaż
- lepszy do dynamiczniej zmieniającego się obrazu, np. podczas lotu drona, który ma wykrywać pojazdy

YOLO11n:

<img width="871" height="139" alt="obraz" src="https://github.com/user-attachments/assets/4c8f9bb3-fdfc-450f-bcff-add3ee980f02" />

- większa dokładność
- mniejszy klatkaż
- lepszy przy wolniejszej zmianie obrazu, lepiej wykrywa szczegóły i mniejsze lub bardziej oddalone pojazdy
