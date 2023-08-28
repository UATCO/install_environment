## Настройка окружения:
Интсрумент позволяет быстро настроить окружение.

### ATTENTION: Для работы нужно установить утилиту make (у linux и mac она скорее всего уже есть):
- для Windows https://gnuwin32.sourceforge.net/packages/make.htm
- для Linux https://ftp.gnu.org/gnu/make/

### Инструкция по применению:
1. Выкачиваем проект https://github.com/UATCO/install_environment.git
2. Открываем и вызываем нужную команду в Makefile / Запускаем командную строку от имени администратора в проекте 
install_environment и вызываем нужную команду в терминале

Доступные команды:
1. Выкачка всех необходимых репозиториев для указанного продукта:
   `make clone`
2. Создание виртуального окружения:
   `make create_venv`
3. Установка зависимостей в виртуальное окружение:
   `make install_requirements`
4. Обновление всех необходимых веток:
   `make pull`

При первом запуске программа попросит ввести проект с которым будем работать и путь куда будем выгружать проект и UATF

[Настройка UATF](https://github.com/UATCO/uatf/blob/master/README.md)

### Доступны следующие продукты:
1) big_geek_tests - [BigGeek](https://biggeek.ru/)