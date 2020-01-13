## Задание 1.
•	Скачал референсный геном и аннотацию (https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13/)

•	Написал annotator.py, которые ищет гены в референсном геноме, координаты которых содержат в себе координаты регионов обогащения

•	Добавил поле, в котором содержится название гена, добавил в файл discripted_target.bad

•	Получил список генов и добавил в файл genes.txt их названия

•	Для того, чтобы узнать список заболеваний, для которых можно использовать данную панель с помощью метода gene set enrichment на сайте http://amp.pharm.mssm.edu/

•	Так же если посмотреть на функции найденых генов, то можно предположить, что их мутации могут привести к аутосомным заболеваниям, в частности к диабету и к гиперинсулинизму

## Задание 2.
•	Сначала хотел использовать выравнивания между целевыми и нецелевыми генами, но в задании написано, что нужно посмотреть 100% гомологию

•	Написал GomologySearch.py, который ищет последовательности в референсном геноме по координатам из файла discripted_target.bad, использовал для этого faidx через samtools командой 
samtools faidx data/GCF_000001405.39_GRCh38.p13_genomic.fna {}:{}-{} >> data/sequences.txt

•	Далее написал класс alignment.py, который ищет одинаковые последовательности у нецелевых и целевых регионов

•	Результаты сохранил в файле matches.txt 

## Что не поучилось/можно сделать лучше
1.	Для поиска в референсном геноме использовал обычный поиск, что с одной стороны хуже, чем бинарный, но с другой стороны для масштабирования алгоритма далее можно распараллелить поиск
2.	*Почти все регионы из таргетной панели удалось найти в аннотации, но
А. Некоторые нашлись несколько раз
Б. Некоторые не нашлись, как мне кажется – это нецелевые регионы
	3.   Все алгоритмы реализованы в методах, что затрудняет их использование
	4.  Файлы задаются вручную, что является минусом для масштабируемости 
![im1](https://github.com/Vasiliy566/parseqLabTest/blob/master/results/Screenshot%202020-01-13%20at%2004.11.34.png)
![im2](https://github.com/Vasiliy566/parseqLabTest/blob/master/results/Screenshot%202020-01-13%20at%2004.11.48.png)

### author
Исаев Василий

Vasyaisaev31@gmail.com

Тестовое задание для parseqLab
