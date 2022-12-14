# ЛАБОРАТОРНАЯ РАБОТА №3
#### Цель: изучить наиболее распространенные помехоустойчивые коды, применяемые в компьютерных сетях для обеспечения целостности пакетов.
#### Лабораторная работа выполняется студентом индивидуально, на базе ПК, по варианту.
#### Задание на лабораторную работу может содержать следующие пункты:
### 1. Данная лабораторная работа может являться продолжением лабораторной работы №2, может выполняться "с нуля".
### 2. Написать коммуникационную программу, позволяющую передать порцию данных между двумя условными либо реальными пользовательскими станциями в закодированном виде, с учетом следующих пунктов задания.
### 3. Программа должна соответствовать однонаправленной топологии point-to-point.
### 4. Программа должна включать передающую, принимающую и создающую ошибки подпрограммы.
### 5. Программа должна иметь отдельное окно ввода для передаваемого текстового сообщения.
### 6. Программа должна иметь отдельное окно вывода для принимаемого текстового сообщения.
### 7. На станции-передатчике сообщение должно разбиваться на блоки фиксированной длины (согласно варианту, информационные полиномы). При "дописывании" предыдущих лабораторных работ должна выдерживаться структура пакета.
### 8. На станции-передатчике и на станции-приемнике должны быть реализованы соответствующие части алгоритма кода Хэмминга либо кода CRC (согласно варианту, должны быть оговорены требования к коду). Алгоритм должен применяться поблочно, при "дописывании" предыдущих лабораторных работ -- попакетно ("охватывать" поля данных из пакетов). Табличные методы вычислений использовать запрещено (например, касательно кода CRC, деление должно выполняться "как на бумаге").
### 9. В программе должна быть предусмотрена подпрограмма -- генератор ошибок, которая должна эмулировать возникновение соответствующего количества ошибок в канале (например, случайным инвертированием битов).
### 10. Программа должна иметь отдельное отладочное окно. В этом окне, по крайней мере, должны отражаться передаваемые закодированные блоки (например, одна строка -- один блок).
### 11. Программа должна работать "циклически".
#### Теоретические основы изложены в лекционном материале и рекомендованной литературе.
