from ultralytics import YOLO
import cv2
import numpy as np

def load_model():
    # Inicializar el modelo YOLO
    model = YOLO("resources/yolov8n.pt")
    return model

def draw_middle_rectangle(frame, center_x, height, color=(0, 255, 0), thickness=2):
    # Calcular las coordenadas del rectángulo en el centro de la imagen
    rect_width = 100  # Ancho del rectángulo, ajusta según tus necesidades
    rect_height = height

    top_left = (int(center_x - rect_width/2), int(frame.shape[0] - rect_height))
    bottom_right = (int(center_x + rect_width/2), int(frame.shape[0]))

    # Dibujar el rectángulo
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)

def detector(cap: object):
    model = load_model()

    # Supongamos que la línea vertical está ubicada en x = 300
    line_x = 300

    # Supongamos que la detección anterior y el contador se almacenan en estas variables
    prev_detection = None
    counter = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("El cuadro de video está vacío o el procesamiento del video se ha completado con éxito.")
            break

        preds = model(frame)

        if len(preds[0].boxes) > 0:
            # Obtener las cajas de detección como un array NumPy
            boxes = preds[0].boxes.xyxy[0].cpu().numpy()

            # Manejar el caso en el que boxes es un array unidimensional
            if boxes.ndim == 1:
                boxes = boxes.reshape((1, -1))

            # Asumiendo que la confianza está en la última columna y el ID de clase en la penúltima columna
            confidences = boxes[:, -1]
            class_ids = boxes[:, 0].astype(int)
            
            class_names = []
            for class_id in class_ids:
                try:
                    class_name = model.names[class_id]
                    class_names.append(class_name)
                except KeyError:
                    print(f"KeyError: Class ID {class_id} not found in model.names")

            # Filtrar personas con confianza mayor o igual a 0.5
            mask = (confidences >= 0.5) & ('person' in class_names)
            filtered_boxes = boxes[mask]

            # Dibujar rectángulo en el centro de la imagen
            draw_middle_rectangle(frame, line_x, height=frame.shape[0])

            # Verificar si la persona cruza la línea desde la derecha hacia la izquierda
            if prev_detection is not None and len(filtered_boxes) > 0:
                prev_x_max = prev_detection[2]
                current_x_min = filtered_boxes[0, 0]

                if prev_x_max > current_x_min and prev_x_max > line_x:
                    counter += 1
                    print("Persona pasó por la caja. Contador actual:", counter)
                elif current_x_min > prev_x_max and prev_x_max < line_x:
                    counter -= 1  # Restar uno al contador

            # Actualizar la detección anterior para el siguiente cuadro
            prev_detection = filtered_boxes[0] if len(filtered_boxes) > 0 else None

            # Mostrar el contador en tiempo real
            cv2.putText(frame, f"Contador: {counter}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Mostrar el cuadro procesado
        cv2.imshow("Object Counting", frame)

        # Salir con 'q' presionado
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    detector(cap)
