## Легенда
То самое место, где хранятся секретные рецепты самого вкусного меда...
## Описание
Небольшой сервис для хранения записей клиентов. Сервис имеет три бд - для хранения паролей (юзер-пароль), для хранения токенов (юзер-md5(salt+username+pass), для хранения записей (токен-запись)
). Запрещен логин по юзернейму admin.
## Решение
Токены генерятся md5(salt+admin+password), т.к. пароль админа - admin регаем юзера admina с паролем dmin и получаем токен админа. Флаг в секрете. 

paseca{th15_h0n3y_t4st35_b4d_c4us3_1t_1s_s4lty_l0000l}