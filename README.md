# cabinet_booking

Сервис должен предоставлять REST API, позволяющее осуществлять бронирование рабочих мест в кабинетах. API должно предоставлять ресурсы для:
1. Бронирования рабочих мест на заданный период времени 
- https://django-booking-rest-api.herokuapp.com/api/v1/booking/create/ (Authenticated only)
2. Просмотра списка бронирований по id рабочего места;
- https://django-booking-rest-api.herokuapp.com/api/v1/workplaces/free/ (Admin only)
3. Авторизации пользователя любым методом (Basic Auth годится);
- https://django-booking-rest-api.herokuapp.com/api/v1/auth/login/ (Login)
- https://django-booking-rest-api.herokuapp.com/api/v1/users/register/ (Register)
4. Ресурс рабочих мест должен иметь 2 необязательных параметра фильтрации: «datetime_from», «datetime_to», ожидающих datetime в формате ISO. Если данные валидны, то ответом на GET с указанными параметрами должен быть список рабочих мест, свободных в указанный временной промежуток. 
- https://django-booking-rest-api.herokuapp.com/api/v1/workplaces/free/
