# https://securepayments.sberbank.ru/wiki/doku.php/integration:api:actioncode
DESCRIPTION_BY_ACTION_CODE = {
    -20010: [
        "Транзакция отклонена по причине того, что размер платежа превысил установленные лимиты Банком-эмитентом.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -9000: [
        "Состояние начала транзакции.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2101: [
        "Блокировка по e-mail",
        "Операция отклонена. Обратитесь в магазин."
    ],

    # в апишке нет такой ошибки, но на деле такая ошибка есть
    # -2024: [
    #     "Отклонено. Frictionless 3D Secure (v.2) запрещен",
    #     "Операция отклонена. Обратитесь в магазин."
    # ],

    -2020: [
        "Получен неверный ECI. Код выставляется в том случае, если пришедший в PaRes ECI не соответствует допустимому значению для данной МПС. Правило работает только для MasterCard (01,02) и Visa (05,06), где значения в скобках - допустимые для МПС.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2019: [
        "PARes от эмитента содержит iReq, вследствие чего платёж был отклонён.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2018: [
        "Directory server Visa или MasterCard либо недоступен, либо в ответ на запрос вовлечённости карты (VeReq) пришла ошибка связи. Это ошибка взаимодействия платёжного шлюза и серверов МПС по причине технических неполадок на стороне последних.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2017: [
        "Отклонено. Статус PARes-а не «Y».",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2016: [
        "Банк-эмитент не смог определить, является ли карта 3dsecure.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2015: [
        "VERes от DS содержит iReq, вследствие чего платёж был отклонён. Операция отклонена.",
        "Обратитесь в банк, выпустивший карту."
    ],

    -2013: [
        "Исчерпаны попытки оплаты.",
        "Операция отклонена. Проверьте введённые данные, достаточность средств на карте и повторите операцию."
    ],

    -2012: [
        "Данная операция не поддерживается.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2011: [
        "Банк-эмитент не смог провести авторизацию 3dsecure-карты.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2010: [
        "Несовпадение XID.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2007: [
        "Истёк срок, отведённый на ввод данных карты с момента регистрации платежа (таймаут по умолчанию - 20 минут; продолжительность сессии может быть указана при регистрации заказа; если у мерчанта установлена привилегия «Нестандартная продолжительность сессии», то берётся период, указанный в настройках мерчанта).",
        "Истёк срок ожидания ввода данных."
    ],

    -2006: [
        "Означает, что эмитент отклонил аутентификацию (3DS авторизация не пройдена).",
        "Операция невозможна. Аутентификация держателя карты завершена неуспешно."
    ],

    -2005: [
        "Означает, что мы не смогли проверить подпись эмитента, то есть PARes был читаемый, но подписан неверно.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    -2003: [
        "Блокировка по порту.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2002: [
        "Транзакция отклонена по причине того, что размер платежа превысил установленные лимиты. Примечание: имеется в виду либо лимиты Банка-эквайера на дневной оборот Магазина, либо лимиты Магазина на оборот по одной карте, либо лимит Магазина по одной операции.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2001: [
        "Транзакция отклонена по причине того, что IP-адрес Клиента внесён в чёрный список.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -2000: [
        "Транзакция отклонена по причине того, что карта внесена в чёрный список.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    -999: [
        "Оплата заказа была отклонена СБОЛ'ом",
        "Платеж СБОЛ отклонен"
    ],

    -100: [
        "Не было попыток оплаты.",
        None
    ],

    0: [
        "Платёж успешно прошёл.",
        None
    ],

    1: [
        "Для успешного завершения транзакции требуется подтверждение личности. В случае интернет-транзакции (соот-но и в нашем) невозможно, поэтому считается как declined.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    5: [
        "Отказ сети проводить транзакцию.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    15: [
        "МПС не смогла определить эмитента карты.",
        "Ошибка проведения платежа. Попробуйте позднее. Если данная ошибка возникла повторно, обратитесь в Ваш банк для разъяснения причин. Телефон банка должен быть указан на обратной стороне карты."
    ],

    53: [
        "Карты не существует в системах процессинга.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    81: [
        "DECLINED_BY_PINPROC Операция отклонена.",
        "Обратитесь в банк, выпустивший карту."
    ],

    100: [
        "Ограничение по карте (Банк эмитент запретил интернет транзакции по карте).",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    101: [
        "Истёк срок действия карты.",
        "Операция отклонена. Проверьте введённые данные, достаточность средств на карте и повторите операцию."
    ],

    103: [
        "Нет связи с Банком-Эмитентом. Торговой точке необходимо связаться с банком-эмитентом.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    104: [
        "Попытка выполнения операции по счёту, на использование которого наложены ограничения.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    106: [
        "Превышено допустимое число попыток ввода ПИН. Вероятно карта временно заблокирована.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    107: [
        "Следует обратиться к Банку-Эмитенту.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    109: [
        "Неверно указан идентификатор продавца/терминала или АСС заблокирован на уровне процессинга.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    110: [
        "Неверно указана сумма транзакции.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    111: [
        "Неверный номер карты.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    116: [
        "Сумма транзакции превышает доступный остаток средств на выбранном счёте.",
        "Операция отклонена. Проверьте введённые данные, достаточность средств на карте и повторите операцию."
    ],

    118: [
        "Сервис не разрешён (отказ от эмитента).",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    119: [
        "Транзакция незаконна.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    120: [
        "Отказ в проведении операции - транзакция не разрешена эмитентом. Код ответа платёжной сети - 57. Причины отказа необходимо уточнять у эмитента.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    121: [
        "Предпринята попытка выполнить транзакцию на сумму, превышающую дневной лимит, заданный банком-эмитентом.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    123: [
        "Превышен лимит на число транзакций: клиент выполнил максимально разрешённое число транзакций в течение лимитного цикла и пытается провести ещё одну.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    125: [
        "Неверный номер карты. Подобная ошибка может означать ряд вещей: Попытка возврата на сумму, больше холда, попытка возврата нулевой суммы. Для AmEx - неверно указан срок действия карты.",
        "Операция отклонена. Проверьте введённые данные, достаточность средств на карте и повторите операцию."
    ],

    208: [
        "Карта утеряна.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    209: [
        "Превышены ограничения по карте.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    400: [
        "Реверсал обработан.",
        None
    ],

    433: [
        "Подозрительный реверсал",
        "Ошибка проведения платежа. Попробуйте позднее. Если данная ошибка возникла повторно, обратитесь в Ваш банк для разъяснения причин. Телефон банка должен быть указан на обратной стороне карты."
    ],

    434: [
        "Ответ получен после реверсала",
        "Ошибка проведения платежа. Попробуйте позднее. Если данная ошибка возникла повторно, обратитесь в Ваш банк для разъяснения причин. Телефон банка должен быть указан на обратной стороне карты."
    ],

    435: [
        "Нет такого кода ответа от сети",
        "Ошибка проведения платежа. Попробуйте позднее. Если данная ошибка возникла повторно, обратитесь в Ваш банк для разъяснения причин. Телефон банка должен быть указан на обратной стороне карты."
    ],

    902: [
        "Ограничение по карте (Владелец карты пытается выполнить транзакцию, которая для него не разрешена).",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    903: [
        "Предпринята попытка выполнить транзакцию на сумму, превышающую лимит, заданный банком-эмитентом.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    904: [
        "Ошибочный формат сообщения с точки зрения банка эмитента.",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    907: [
        "Нет связи с Банком, выпустившим Вашу карту. Для данного номера карты не разрешена авторизация в режиме stand-in (этот режим означает, что эмитент не может связаться с платёжной сетью и поэтому транзакция возможна либо в оффлайне с последующей выгрузкой в бэк офис, либо она будет отклонена).",
        "Нет связи с банком. Повторите позже."
    ],

    909: [
        "Невозможно провести операцию (Ошибка функционирования системы, имеющая общий характер. Фиксируется платёжной сетью или банком-эмитентом).",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    910: [
        "Банк-эмитент недоступен.",
        "Нет связи с банком. Повторите позже."
    ],

    913: [
        "Неверный формат сообщения (Неправильный формат транзакции с точки зрения сети).",
        "Операция отклонена. Обратитесь в банк, выпустивший карту."
    ],

    914: [
        "Не найдена транзакция (когда посылается завершение или reversal или refund).",
        "Операция отклонена. Обратитесь в магазин."
    ],

    999: [
        "Отсутствует начало авторизации транзакции. Отклонено по фроду или ошибка 3dsec. После получения этого кода ответа дальнейшие попытки проведения платежа отклоняются.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    1001: [
        "Пусто (Выставляется в момент регистрации транзакции, т.е. когда еще по транзакции не было введено данных карт).",
        "Не получен ответ от банка. Повторите позже."
    ],

    2002: [
        "Неверная операция.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2003: [
        "SSL (Не 3d-Secure/SecureCode) транзакции запрещены Магазину.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2004: [
        "Оплата через SSL без ввода CVС2 запрещена.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2005: [
        "Платёж не соответствует условиям правила проверки по 3ds.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2006: [
        "Однофазные платежи запрещены.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2008: [
        "Транзакция ещё не завершена.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2009: [
        "Сумма возврата превышает сумму оплаты.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2014: [
        "Ошибка выполнения 3DS-правила.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2015: [
        "Ошибка выполнения правила выбора терминала (правило некорректно).",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2016: [
        "Мерчант не имеет разрешения на 3-D Secure, необходимое для проведения платежа.",
        "Операция отклонена. Обратитесь в магазин."
    ],

    2022: [
        "Заказ отклонён.",
        "Отклонён."
    ],

    2023: [
        "Очередь на запросов на обработку в процессинг превысила допустимый лимит.",
        "Ошибка проведения платежа. Попробуйте позднее."
    ],

    4005: [
        "Заказ отклонён продавцом.",
        "Отклонено продавцом."
    ],

    71015: [
        "Введены неправильные параметры карты.",
        "Операция отклонена. Проверьте введённые данные, достаточность средств на карте и повторите операцию."
    ],

    151018: [
        "Таймаут в процессинге. Не удалось отправить.",
        "Не получен ответ от банка. Повторите позже."
    ],

    151019: [
        "Таймаут в процессинге. Удалось отправить, но не получен ответ от банка.",
        "Не получен ответ от банка. Повторите позже."
    ],

    341014: [
        "Код отказа РБС.",
        "Операция отклонена. Обратитесь в магазин."
    ]
}
