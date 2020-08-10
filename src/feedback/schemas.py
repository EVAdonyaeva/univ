class TicketPostRequest(serializers.Serializer):
    checkIn = serializers.DateTimeField(required=True, label='Дата заселения')
    checkOut = serializers.DateTimeField(required=True, label='Дата выселения')
    hotelCode = serializers.CharField(required=True, label='Код отеля')
    adultsCount = serializers.IntegerField(required=True, label='Количество взрослых, 1-10')
    childrenCount = serializers.IntegerField(required=False, label='Количество детей, 0-10')
    roomsCount = serializers.IntegerField(required=True, label='Количество номеров, 1-10')
    roomClass = serializers.CharField(required=True, label=f'Класс номера: {VALID_ROOM_CLASSES}')
    userComment = serializers.CharField(required=False, label='Комментарий пользователя', allow_null=True,
                                        allow_blank=True)