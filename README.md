## Развертывание
1 - Выполнить команды первичного развертывания:
```shell script
sudo git clone https://github.com/flatdragon/docker-flask-sqlite.git
cd docker-flask-sqlite
sudo docker-compose up --build -d
```
2 - Несколько раз посетить страницу (демонстрация счетчика): http://localhost

3 - Выполнить команду остановки и удаления контейнеров проекта:
```shell script
sudo docker-compose down
```
4 - Выполнить команду остановки и удаления контейнеров проекта:
```shell script
sudo docker-compose up --build -d
```
5 - Несколько раз посетить страницу (чтобы убедиться в персистентности базы данных): http://localhost
