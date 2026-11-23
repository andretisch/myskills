#!/usr/bin/env python3
from fpdf import FPDF

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
OUT = "/workspace/Тишкин Андрей.pdf"


class PDF(FPDF):
    def header(self):
        pass


def section_title(pdf, text):
    pdf.set_font("CV", style="B", size=11)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(200, 200, 200)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(3)


def body(pdf, text, bold=False):
    pdf.set_font("CV", style="B" if bold else "", size=9)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(0, 4.5, text)
    pdf.ln(2)


def main():
    pdf = PDF()
    pdf.add_font("CV", "", FONT)
    pdf.add_font("CV", "B", FONT_B)
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()
    pdf.set_margins(14, 12, 14)

    pdf.set_font("CV", "B", 18)
    pdf.cell(0, 10, "АНДРЕЙ ТИШКИН", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("CV", "B", 12)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 7, "ML Engineer · Computer Vision · Edge Inference", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("CV", "", 9)
    pdf.cell(0, 5, "+7 (904) 683-97-73  ·  a@aphl.ru  ·  @redeyex  ·  github.com/andretisch", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    section_title(pdf, "СЕЙЧАС")
    body(
        pdf,
        "ООО «Ви Фрай» (We Fry), с 12.08.2026 — инженер-программист по ИИ.\n"
        "Промышленное CV на SAM 3: RTSP, edge-инференс без облачного GPU, мониторинг потоков, "
        "подготовка к тиражированию. Параллельно: архитектура LLM (Ollama, MCP, 1С:ERP).",
    )

    section_title(pdf, "О СЕБЕ")
    body(
        pdf,
        "Разработчик ML/CV с акцентом на промышленную безопасность и видеоаналитику на edge. "
        "Реализовал детекцию СИЗ на производстве (YOLO, RTSP, CPU-оптимизация, ONNX/OpenVINO), "
        "проекты с компьютерным зрением и нейроассистентами. 14+ лет опыта в ИТ-инфраструктуре "
        "и ERP — умею доводить модель до стабильной работы на объекте.",
    )

    section_title(pdf, "НАВЫКИ")
    body(
        pdf,
        "Python · PyTorch · OpenCV · Ultralytics YOLO · SAM 3\n"
        "ONNX · ONNX Runtime · OpenVINO · RTSP · FFmpeg\n"
        "Метрики: mAP, precision, recall · аугментации · Docker · Linux · Git\n"
        "Доп.: LangChain, RAG, FAISS, QLoRA (Qwen) · Zabbix (мониторинг сервисов)",
    )

    section_title(pdf, "ОПЫТ РАБОТЫ")
    jobs = [
        (
            "08.2026 — н.в.  ·  ООО «Ви Фрай» (We Fry)  ·  Инженер-программист по ИИ",
            "SAM 3, RTSP, edge CV на производстве. Архитектура локальных LLM и интеграция с 1С:ERP.",
        ),
        (
            "02.2025 — 05.2025  ·  ООО «Картика»  ·  Data Scientist (проект)",
            "Детекция СИЗ на производстве: дообучение YOLO, mAP/precision/recall по классам, "
            "оптимизация инференса на CPU, ONNX/OpenVINO, эмуляторы RTSP, документация для объекта.",
        ),
        (
            "05.2025 — 08.2026  ·  ООО «Кузминки»  ·  Руководитель ИТ",
            "Пилоты YOLO, Qwen, LLM; Linux, PostgreSQL, Proxmox.",
        ),
        (
            "05.2024 — 08.2024  ·  ООО «КСК ИТ»  ·  Data Scientist (проект)",
            "YOLOv5n для ГРЗ, оптимизация скорости, HTTP API, утилиты тестирования.",
        ),
        (
            "11.2024 — 01.2025  ·  ООО «Юнилайт»  ·  Data Scientist (проект)",
            "Оптимизация RAG, база знаний.",
        ),
        (
            "08.2023 — 10.2023  ·  Kia Russia & CIS  ·  Data Scientist (проект)",
            "GPT-ассистент, LangChain, FAISS, парсер сайта.",
        ),
        (
            "Pet-проект: дообучение Qwen (QLoRA)",
            "Повысил точность в 2–3 раза на русском датасете, запуск на CPU.",
        ),
    ]
    for title, desc in jobs:
        body(pdf, title, bold=True)
        body(pdf, desc)
        pdf.ln(1)

    section_title(pdf, "ОБРАЗОВАНИЕ")
    body(
        pdf,
        "2024 — Университет ИИ: Data Science, ML, AI Engineer\n"
        "2018 — ТИЭИ: системный администратор\n"
        "2008 — ЛМК, механический\n"
        "2016 — Geekbrains",
    )

    section_title(pdf, "ВАКАНСИЯ: ML ENGINEER (EDGE INFERENCE)")
    body(
        pdf,
        "Удалённо · МСК ±2 · созвоны 2× в неделю · ГПХ · готов к оплачиваемому тестовому · ASAP",
    )

    pdf.output(OUT)
    print(OUT)


if __name__ == "__main__":
    main()