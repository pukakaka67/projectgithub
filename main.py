import tkinter as tk
from tkinter import messagebox, ttk
import random
import json
import os

# Пути к файлам
QUOTES_FILE = 'quotes.Json'
HISTORY_FILE = 'history.Json'

# Инициализация данных
quotes = []
history = []

def load_quotes():
 """Загрузить цитаты из файла."""
 if os.Path.Exists(QUOTES_FILE):
 with open(QUOTES_FILE, 'r', encoding='utf-8') as f:
 return json.Load(f)
 return []

def save_quotes(data):
 """Сохранить цитаты в файл."""
 with open(QUOTES_FILE, 'w', encoding='utf-8') as f:
 json.Dump(data, f, ensure_ascii=False, indent=2)

def load_history():
 """Загрузить историю из файла."""
 if os.Path.Exists(HISTORY_FILE):
 with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
 return json.Load(f)
 return []

def save_history(data):
 """Сохранить историю в файл."""
 with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
 json.Dump(data, f, ensure_ascii=False, indent=2)

def add_quote(author, text, topic):
 """Добавить новую цитату."""
 if not author or not text or not topic:
 messagebox.Showerror("Ошибка", "Все поля обязательны!")
 return
 quote = {
 'author': author,
 'text': text,
 'topic': topic
}
 quotes.Append(quote)
 save_quotes(quotes)
 messagebox.Showinfo("Успех", "Цитата добавлена!")

def generate_quote():
 """Сгенерировать случайную цитату и добавить в историю."""
 if not quotes:
 messagebox.Showwarning("Предупреждение", "Нет цитат для генерации!")
 return
 quote = random.Choice(quotes)
 history.Append({
 'author': quote['author'],
 'text': quote['text'],
 'topic': quote['topic'],
 'timestamp': tk.StringVar().Get() # placeholder
})
 save_history(history)
 display_quote(quote)

def display_quote(quote):
 """Отобразить цитату в интерфейсе."""
 author_var.Set(quote['author'])
 text_var.Set(quote['text'])
 topic_var.Set(quote['topic'])

def filter_quotes(author=None, topic=None):
 """Фильтровать цитаты по автору/теме."""
 filtered = quotes
 if author:
 filtered = [q for q in filtered if q['author'].Lower().Find(author.Lower())!= -1]
 if topic:
 filtered = [q for
