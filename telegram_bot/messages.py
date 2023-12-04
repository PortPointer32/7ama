from telegram_bot.utils import StatesUsers

# СООБЩЕНИЯ ОТ БОТА
start_message = """<b>Вас приветствует магазин -</b>\nhttps://amz24.biz/\n\n<b>Наши контакты:</b>\nJabber:\nTelegram:\nСайт автопродаж - https://amz2.biz/\n\nУдачных покупок!
➖
Привет, <b>%s</b>
Ваш баланс: 💰0 руб.
➖
Для просмотра полного сообщения (с контактами магазина и командами бота) отправьте 👉 @@
➖➖
Для управления персональными ботами нажмите 👉 /mybots
Для добавления персонального бота нажмите 👉 /addbot
Чтобы заработать денег нажмите 👉 /ref
➖
<b>Выберите город:</b>"""
start_2_message = """🏠 Город: %s
➖-
Выберите товар:"""
not_command_message = "Такой команды нет\nПиши /start"
poll_message = """Нет активных голосований.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
ref_message = """💰 Уважаемые клиенты! Делитесь своими ботами с друзьями и получайте 50 руб. с каждого его оплаченного заказа на минимальную сумму от 1500 руб.
➖➖
Для этого просто добавьте персонального бота, с помощью команды /addbot и переведите его в режим "Отвечать всем", с помощью команды /editbot
Либо если у Вас уже добавлен бот, то просто переведите его в режим "Отвечать всем", но советуем лучше иметь 2 бота - один лично для Вас, который отвечает только Вам, а второй для друзей, который отвечает всем.
➖➖
Успехов!
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
balance_message = """Ваш баланс:
💰0 руб.
➖
Для пополнения баланса нажмите 👉/pay или !
Для просмотра баланса нажмите 👉/balance или =
Для просмотра истории операций по счету нажмите 👉/history или *
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
check_message = """➖➖
Если Вы произвели оплату и закрыли страницу:
➖➖
👉 Просто отправьте 
/checkXXXX_XXXXXXXXX (номер заказа_комментарий), например 
/check1234_5678910, чтобы проверить статус заказа и получить адрес. Номер заказа и комментарий Вы получаете на странице оплаты заказа, где выдаются реквизиты, обязательно сохраните эти данные перед оплатой.
➖➖
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
help_message = """Добро пожаловать в наш магазин.
Уважаемый клиент, будьте внимательны при оплате и выборе товара.
Перед покупкой товара, бот предложит Вам город, товар и удобный для Вас район, после чего, выдаст реквизиты для оплаты.
Внимательно перед покупкой проверяйте товар и выбранный район. Обязательно записывайте реквизиты для оплаты (номер кошелька и комментарий).

При оплате, Вам необходимо обязательно указатькомментарий, который выдал Вам бот, иначе оплата не будет засчитана в автоматическом режиме и Вы не получите адрес.
Всегда записывайте номер заказа и комментарий, с помощью них, вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства. Сохраняйте чек до тех пор, пока не получили адрес. Присутствует возможность производить несколько платежей с одним комментарием. Платежи суммируются и в случае, если сумма полная - Вы получаете свой адрес.
Будьте внимательны, кошелек, комментарий и сумма должны быть точными. Если возникли какие-либо проблемы - обращайтесь к оператору.

После внесения оплаты, нажмите кнопку проверки платежа и если Ваша оплата будет найдена - Вы получите адрес в автоматическом режиме.
Так же для Вашего удобства реализована возможность просмотра Вашего последнего заказа, для этого необходимо нажать /lastorder
А для того, чтобы вернуться на стартовую страницу к выбору городов, просто нажмите /start или напишите любое сообщение.

Нужные команды:
/connect - выводит все доступные команды для связи с Администрацией
/ticket - создать тикет с Администрацией
/mytickets - последние 10 тикетов
/myissues - последние 10 заявок по ненаходам
/myextickets - последние 10 зависших платежей на обменник
Приятных покупок!
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
connect_message = """Чтобы посмотреть список тикетов нажмите 👉 /mytickets
Чтобы создать тикет нажмите 👉 /ticket
➖➖
Чтобы посмотреть список заявок на перезаклад нажмите 👉 /myissues
Чтобы создать заявку на перезаклад нажмите 👉 /issue
➖➖
Чтобы посмотреть список обращений по зависшим платежам нажмите 👉 /myextickets
Чтобы создать обращение по зависшему платежу нажмите 👉 /exticket
➖➖
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
history_message = """История пополнений и расходов:
➖➖➖
Операции не найдены
➖➖➖
Для пополнения баланса нажмите 👉/pay или !
Для просмотра баланса нажмите 👉/balance или =
Для просмотра истории операций по счету нажмите 👉/history или *
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
addreview_message = """Количество отзывов не может превышать количество покупок.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
lastorder_message = """У вас нет заказов.

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
issue_message = """Вы еще не делали заказов чтобы создавать заяки на перезаклад
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
myissues_message = """Заявки не найдены
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

captha_message = "Привет\nПожалуйста, решите капчу с цифрами на этом изображении, чтобы убедиться, что вы человек."

pay_message = """Выберите метод пополения баланса:
➖➖➖
<b>Bitcoin</b>
[Для выбора нажмите 👉 /pay1]
➖➖➖
<b>Litecoin</b>
[Для выбора нажмите 👉 /pay5]
➖➖➖
<b>Банковская карта</b>
[Для выбора нажмите 👉 /pay2]
➖➖➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

pay1_1_message = """❗️ Важно! Перед покупкой прочитайте мануал "Как купить Bitcoin за 15 секунд", нажмите на ссылку ниже:
➖➖➖➖
http://telegra.ph/Kak-kupit-Bitcoin-za-15-sekund-05-14-2
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay1_2_message = """Курс 1 BTC = %s рублей.
➖➖
На какую сумму в рублях Вы хотите пополнить баланс?
➖➖
В ответном сообщени, отправьте просто цифру, например 1000
Напоминаем, что минимальная сумма пополнения через <b>Bitcoin - %s</b> рублей.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay5_2_message = """Курс 1 LTC = %s рублей.
➖➖
На какую сумму в рублях Вы хотите пополнить баланс?
➖➖
В ответном сообщени, отправьте просто цифру, например 1000
Напоминаем, что минимальная сумма пополнения через <b>Litecoin - %s</b> рублей.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay2_1_message = """<b>❗️Внимание!Перед пополнением, обязательно ознакомьтесь с правилами.Нажимая кнопку "Пополнить" - Вы автоматически соглашаетесь с данными правилами.</b>

Введите сумму в рублях, на которую Вы хотите пополнить баланс, ознакомьтесь с правилами и только после этого нажмите кнопку <b>❗️"Пополнить". В следующем окне система выдаст точную сумму к оплате (с учетом комиссии) и реквизиты. Реквизиты актуальны 30 минут, после чего заявка на пополнение будет удалена и деньги не будут возвращены. Оплата должна быть одним переводом. Если будет несколько переводов - оплата не зачтется и деньги не вернутся.</b>

Пополнение баланса происходит только после поступления <b>❗️ТОЧНОЙ СУММЫ</b> денег на баланс банковской карты! Обычно это занимает 2-3 минуты.

<b>❗️Нажимайте "Я оплатил", только после реальной оплаты.</b> Если после нажатия "Я оплатил" система не увидит Вашу оплату в течении 30 минут, ваш заказ будет отменен и Вы не получите деньги на баланс.

Пополнить банковскую карту можно любым удобным способом, например: со своего QIWI-кошелька, терминала, банковской карты (card2card), Yandex.Деньги, Payeer, WebMoney и другие платежные системы.

При пополнении - переводите обязательно <b>❗️ТОЧНУЮ сумму,</b> которую Вам выдал сайт вместе с реквизитами! Многие терминалы берут комиссию и с них сложно оплатить точную сумму, старайтесь этого избегать. Важно!

<b>❗️Кнопка "Я оплатил" нажимается в самый последний момент, когда Вы произвели оплату и уверены в точной сумме.</b>

При точном выполнении всех правил - Ваш баланс будет мгновенно пополнен! Вопросы по зависшим платежам принимаются в течении суток с момента оплаты. Если Ваш баланс не был пополнен и Вы реально перевели деньги на выданные Вам реквизиты - свяжитесь со службой поддержки обменника на вкладке "Завис платеж?" или "Заявки на покупки и пополнения", либо в боте команда /exticket и обязательно укажите номер заявки и детали вашего платежа вместе с точной суммой оплаты. Скриншоты чеков обязательны! По истечении суток запросы по зависшим платежам не принимаются! Заявки на пополнение баланса обрабатываются через сторонний обменник, если Вы создали обращение по зависшему платежу и Вашу проблему не решили - обратитесь к Администрации магазина во вкладке "Тикеты", либо в боте команда /ticket

По истечении суток запросы по зависшим платежам не принимаются!

Заявки обрабатываются через сторонний обменник, если Вы создали обращение по зависшему платежу и Вашу проблему не решили - обратитесь к Администрации магазина

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay2_2_message = """Минимальная сумма для пополнения:
<b>❗️ %s рублей.</b>
Максимальная сумма для пополнения:
<b>❗️ 100 000 рублей.</b>
➖
Введите сумму, на которую хотите пополнить баланс
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay3_1_message = """<b>❗️Внимание! Перед пополнением, обязательно ознакомьтесь с правилами. Нажимая кнопку "Пополнить" - Вы автоматически соглашаетесь с данными правилами.</b>

Введите сумму в рублях, на которую Вы хотите пополнить баланс, ознакомьтесь с правилами и только после этого нажмите кнопку <b>❗️"Пополнить". В следующем окне система выдаст точную сумму к оплате (с учетом комиссии) и реквизиты. Реквизиты актуальны 30 минут, после чего заявка на пополнение будет удалена и деньги не будут возвращены. Оплата должна быть одним переводом. Если будет несколько переводов - оплата не зачтется и деньги не вернутся.</b>

Пополнение баланса происходит только после поступления <b>❗️ТОЧНОЙ СУММЫ</b> денег на баланс мобильного телефона! Обычно это занимает 30-60 секунд.

<b>❗️Нажимайте "Я оплатил", только после реальной оплаты.</b> Если после нажатия "Я оплатил" система не увидит Вашу оплату в течении 3х минут, ваш заказ будет отменен и Вы не получите деньги на баланс.

Оплата принимается только на <b>❗️НОМЕР МОБИЛЬНОГО ТЕЛЕФОНА.</b> Пополнять выданный номер можно любым способом, например через терминал, офис мобильного оператора, банковской картой, QIWI и так далее.

<b>❗️Не переводите деньги на QIWI или любую другую платежную систему вы их теряете БЕЗ ВОЗМОЖНОСТИ ВОЗВРАТА!</b>

При пополнении - переводите обязательно <b>❗️ТОЧНУЮ сумму</b>, которую Вам выдал сайт вместе с реквизитами! Многие терминалы берут комиссию и с них сложно оплатить точную сумму, старайтесь этого избегать. <b>❗️Важно! Если по какой-либо причине Вы отправили не точную сумму - воспользуйтесь кнопкой "Изменить сумму" и введите правильную сумму (которую Вы отправили или которую зачислил терминал). Только после того, как Вы уверены в сумме - нажмите кнопку "Я оплатил".</b>

Внимание! Если Вы не можете получить реквизиты, то сделайте отмену и создайте заявку с другой уникальной суммой! Например если вы создали заявку на 1500 рублей и не можете получить реквизиты, то сделайте отмену и создайте заявку на 1531 или 1532 рубля.

<b>❗️Кнопка "Я оплатил" нажимается в самый последний момент, когда Вы произвели оплату и уверены в точной сумме. При точном выполнении всех правил - Ваш баланс будет мгновенно пополнен!</b>

Вопросы по зависшим платежам принимаются в течении суток с момента оплаты. Если Ваш баланс не был пополнен и Вы реально перевели деньги на выданные Вам реквизиты - свяжитесь со службой поддержки обменника на вкладке "Завис платеж?" или "Заявки на покупки и пополнения", либо в боте команда /exticket и обязательно укажите номер заявки и детали вашего платежа вместе с точной суммой оплаты. Скриншоты чеков обязательны! По истечении суток запросы по зависшим платежам не принимаются! Заявки на пополнение баланса обрабатываются через сторонний обменник, если Вы создали обращение по зависшему платежу и Вашу проблему не решили - обратитесь к Администрации магазина во вкладке "Тикеты", либо в боте команда /ticket

Заявки обрабатываются через сторонний обменник, если Вы создали обращение по зависшему платежу и Вашу проблему не решили - обратитесь к Администрации магазина


Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay4_1_message = """Для пополнения баланса с помощью купона, необходимо отправить код купона, после чего Ваш баланс моментально будет пополнен на сумму купона, который Вы активировали.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

not_count_message = """Что то пошло не так!
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
min_count_message = """Ошибка. Укажите правильную сумму пополнения. Минимальная сумма пополнения через <b>%s - %s</b> рублей.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

pay1_what_pay_message = "<b>Bitcoin</b>"
pay5_what_pay_message = "Litecoin"
pay2_what_pay_message = "<b>Банковскую карту</b>"
not_coupon_message = """Ошибка. Купон не найден
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay1_3_message = """Для пополнения баланса оплатите:
➖➖
💰 <code>%s</code> BTC
➖➖
На Bitcoin кошелёк:
➖➖
👉 <code>%s</code>
➖➖
Переведите Bitcoin на указаный кошелек и просто ожидайте 1 подтверждения в сети Bitcoin - система автоматически зачислит Вам баланс и отправит сообщениеоб успешном пополнении баланса.
➖➖
Это Ваш постоянный Bitcoin кошелек для пополнения баланса Вашего личного кабинета. Чтобы пополнить баланс в магазине, просто отправьте на данный кошелек средства, после 1 подтверждения - система зачислит Вам баланс в автоматическом режиме. Вы можете отправлять любое количество Bitcoin на Ваш кошелек - система автоматически расчитает Вам баланс в рублях, по курсу Bitcoin на момент Вашего перевода. Старайтесь пополнять всегда немного больше сумму (например на 20-30 рублей больше), так как курс Bitcoin может измениться в момент Вашего перевода и Вам может не хватить денег для покупки товара.
➖➖
Для пополнения баланса нажмите 👉/pay
Для просмотра баланса нажмите 👉/balance
Для просмотра истории операций по счету 👉/history
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay5_3_message = """Для пополнения баланса оплатите:
➖➖
💰 <code>%s</code> LTC
➖➖
На litecoin кошелёк:
➖➖
👉 <code>%s</code>
➖➖
Переведите Litecoin на указаный кошелек и просто ожидайте 1 подтверждения в сети Litecoin - система автоматически зачислит Вам баланс и отправит сообщениеоб успешном пополнении баланса.
➖➖
Это Ваш постоянный Litecoin кошелек для пополнения баланса Вашего личного кабинета. Чтобы пополнить баланс в магазине, просто отправьте на данный кошелек средства, после 1 подтверждения - система зачислит Вам баланс в автоматическом режиме. Вы можете отправлять любое количество Litecoin на Ваш кошелек - система автоматически расчитает Вам баланс в рублях, по курсу Litecoin на момент Вашего перевода. Старайтесь пополнять всегда немного больше сумму (например на 20-30 рублей больше), так как курс Litecoin может измениться в момент Вашего перевода и Вам может не хватить денег для покупки товара.
➖➖
Для пополнения баланса нажмите 👉/pay
Для просмотра баланса нажмите 👉/balance
Для просмотра истории операций по счету 👉/history
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
pay2_3_message = """Заявка на пополнение через <b>%s</b>:
👉 # %s
Сумма для оплаты:
💰 %s руб.
Номер %s для оплаты:
👉 %s
➖➖➖➖
❗️ Реквизиты действительны в течении 30 минут!
➖➖➖➖
👉 На Ваш баланс будет зачислено %s руб.
➖➖➖➖
Для пополнения баланса нажмите 👉/pay
Для просмотра баланса нажмите 👉/balance
Для просмотра истории операций по счету 👉/history
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
trans_non_message = """Заявки не найдены
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
trans_message = """История заявок на покупки или пополнение баланса через SIM или банковскую карту:
➖
Показываются последние 10 заявок."""
reviews1_message = """🏃 Автор: 5********6
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все на месте. Продолжай в том же духе. Стаф хороший

➖

🏃 Автор: L********1
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Чуть чуть не по метке. Съём очень лёгкий, кач хороший.

➖

🏃 Автор: 7*******2
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2.01гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

В касание

➖

🏃 Автор: A*******o
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Всем привет магазин хороший, всё устраивает, цена и стаф, за всё время было пару ненаходов и то по мелочевке!

➖

🏃 Автор: d************o
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все четко

➖

🏃 Автор: 5********6
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Дома )еще не пробовал но в качестве не сомневаюсь

➖

🏃 Автор: 4*******3
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2.01гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

В касание,побольше таких кладов.

➖

🏃 Автор: 6********3
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️

Нашёл. Брал прикоп, а в итоге клад висел на ветках травы.

➖

🏃 Автор: x************7
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1гр
📆 Дата: %s
📊 Оценка: ⭐️

Пришел , а на месте нет клада , заебсиь съездил потратил нервы на раскопки очень расстроен

👨 Ответ: Откройте заявку на перезаклад, мы Вам поможем!

➖

🏃 Автор: A******6
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Место кайфовое, безлюдное, съем легчайший.🤝

➖
Чтобы добавить отзыв нажмите 👉 /addreview
➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
reviews2_message = """🏃 Автор: J********7
🏢 Город: Советск
🍕 Товар: Меф Crystal 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

10/10

➖➖➖

🏃 Автор: J********7
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

В подобных кладах необходимо дальний ракурс фото, а не просто ствол дерева. Кач 10/10

➖➖➖

🏃 Автор: J********7
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все четко👌🏻

➖➖➖

🏃 Автор: B******f
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️

км скинул напротив места где сидят и отдыхают люди, потратил полтора часа своего времени на снятие, неприятно. Вес норм, кач топ.

➖➖➖

🏃 Автор: S*************7
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1.01гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Чётко, точно, близко!! Красивая работа👍

➖➖➖

🏃 Автор: T*************i
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Забрал.все четко, все дома.

➖➖➖

🏃 Автор: T************2
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Всё норм в касание

➖➖➖

🏃 Автор: 2*******2
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

В касание! Красавцы пацаны. Жду купон!

➖➖➖

🏃 Автор: 7*******2
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1.01гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все в поряде👍 В касание🔥 Может порадуете купончиком?)

➖➖➖

🏃 Автор: 1********0
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Всё прошло успешно. Спасибо

➖➖➖
Чтобы добавить отзыв нажмите 👉 /addreview
➖➖➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
reviews3_message = """🏃 Автор: D***********1
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1.01гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Всё чётко, кура красавчик

➖➖➖

🏃 Автор: 5********4
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

На месте 👍

➖➖➖

🏃 Автор: 3*******1
🏢 Город: Советск
🍕 Товар: Меф Crystal 1гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Изи катка в касание ,спасибо ,еще и камнем целом !!!

➖➖➖

🏃 Автор: 5********3
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

76753.спасибо в касание

➖➖➖

🏃 Автор: A******6
🏢 Город: Советск
🍕 Товар: MEPHEDRONE CRYSTAL ICE 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Успешно 

➖➖➖

🏃 Автор: A*****a
🏢 Город: Киров
🍕 Товар: Меф Crystal 2гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все четко кач бомба, подъем изи место антишкур. Но недавно брат ед. приехал забирать через сутки и не нашёл будто и не было.)

➖➖➖

🏃 Автор: b***4
🏢 Город: Киров
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Все ровно магаз четкий как всегда в касашку 
Кач мощный

➖➖➖

🏃 Автор: A**************o
🏢 Город: Киров
🍕 Товар: Меф Crystal 1гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Дома.
Нашёл легко от души)
Можно просьбу (поменьше леса) ночью стрёмно идти за целью
А так став отменный.

➖➖➖

🏃 Автор: A******6
🏢 Город: Киров
🍕 Товар: MEPHEDRONE CRYSTAL ICE 1гр
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Скатался на край света, удачно.

➖➖➖

🏃 Автор: S*******3
📆 Дата: %s
📊 Оценка: ⭐️⭐️⭐️⭐️⭐️

Балдеж малдеж

➖➖➖
Чтобы добавить отзыв нажмите 👉 /addreview
➖➖➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
addbot_message = """✌️ Отправьте API Token своего Telegram бота в ответном сообщении:
➖➖➖
Если у Вас нет своего API Token'а или Вы не знаете, что это такое, тогда прочитайте <b>подробную инструкцию</b> <a href="https://telegra.ph/Instrukciya-po-sozdaniyu-personalnogo-Telegram-bota-04-26-2">здесь</a>
➖➖➖
1. Воспользуйтесь официальным Telegram аккаунтом для создания ботов - @BotFather
➖➖➖
2. Отправьте ему команду /newbot.
➖➖➖
3. Далее он попросит Вас придумать имя для Вашего бота.
➖➖➖
4. Далее он попросит Вас придумать username для Вашего бота. Обратите внимание, username должен ОБЯЗАТЕЛЬНО заканчиваться словом bot
➖➖➖
5. Скопируйте свой API Token и отправьте его нашему боту в ответ на это сообщение.
➖➖➖
Вам необходимо получить свой API Token самостоятельно, только после этого, Вы сможете добавить своего персонального бота, выше описан процесс, что Вам необходимо сделать, чтобы получить API Token
Если Вы все сделаете верно, то Вам пришлют API Token, выглядить он примерно так - 1542120167:SFQ8ELnPFEQSQChTFEQLGQSXlImiU1f3F2a (не используйте данные токен, это пример, он работать не будет - Вам необходимо получить свой)
➖➖➖
Внимание! Добавлять и управлять своими персональными ботами можно через команды /addbot, /mybots
➖➖➖
Для того, чтобы все уведомления приходили в Ваш персональный бот - ни в коем случае не меняйте ник или токен своего персонального бота, иначе сам бот и уведомления перестанут работать!
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
success_add_bot_message = """Ваш API Token успешно сохранен. Вы можете обратиться к своему боту @%s прямо сейчас.
➖➖➖
Если Вы не планируете делиться своим ботом с друзьями, оставьте все как есть - Ваш персональный бот уже работает.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
error_add_bot_message = """API Token не корректен
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
there_is_bot_message = """Указанный API Token уже используется. Используйте другой API Token
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_my_bots_message = """Приватные боты не найдены. Используйте команду /addbot чтобы добавить приватного бота.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
my_bot_1_message = """💰 У магазина работает реферальная программа.
➖➖➖➖
За привлеченых новых клиентов с каждой их покупки больше 1500 руб. вы будете получать 50 руб. на Ваш баланс.
➖➖➖➖
Ваши приватные боты:
➖➖➖➖"""
my_bot_2_message = """
➖➖➖➖
Если вы хотите добавить бота, используйте команду /addbot
Если вы хотите удалить бота, используйте команду /removebot
➖➖➖➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
exticket_message = """Отправьте номер заявки на пополнение по которой Вам не зачислили деньги на баланс (только цифры), либо номер заказа по которому не был выдан адрес при оплате через SIM или Банковскую карту (только цифры). Обратите внимание, отправлять номера заявок и заказов повторно - запрещено! Одна заявка = одно обращение.
➖➖➖
Внимание! Перед созданием заявки, приготовьте следующие материалы:
➖➖➖
👉 Номер заявки
👉 Фото чека
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
success_exticket_message = """Отправьте фото чека и подождите
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_exticket_message = """Вы еще не делали пополнений чтобы создавать обращения
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
error_exticket_messsage = """Заявка не найдена. Введите правильный номер заявки
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_photo_message = """Изображение не корректно. Попробуйте еще раз
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
success_photo_message = """Напишите Ваш комментарий, например:
➖➖➖
01 января 1970 года в ___ ч.___ мин. создал заявку на пополнение №ХХХХ. Возникли следующие проблемы :_________________________________
Комментарий отправляется одним сообщением, дополнение или изменение комментария невозможны.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
exticket_send_message = """Ваше обращение отправлено. Служба поддержки обменника свяжется с Вами в ближайшее время.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
exticket_in_message = """По данной заявке уже создано обращение. Введите другой номер заявки
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_myexticket_message = """Обращения не найдены
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_myextickets_message = """Обращение не найдено
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
removebot_message = """Отправьте номер бота, которого хотите удалить.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_removebot_message = """Приватные боты не найдены. Используйте команду /addbot чтобы добавить приватного бота.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
success_removebot_message = """Приватные бот Удалён!
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
not_city_message = """Выберите %s строго из списка
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_product_message = """🏠 Город: <b>%s</b>
🏃 Район: <b>%s</b>
🎁 Название: <b>%s</b>
💰 Стоимость: <b>%s</b>
➖➖
Выберите метод оплаты:
➖➖
<b>Bitcoin</b>
[Для выбора нажмите 👉 /buy1 ]
➖➖
<b>Litecoin</b>
[Для выбора нажмите 👉 /buy2 ]
➖➖
<b>Банковская карта</b>
[Для выбора нажмите 👉 /buy3 ]
➖➖

Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_1_message = """🏠 Город: <b>%s</b>
🏃 Район: <b>%s</b>
🎁 Название: <b>%s</b>
💰 Стоимость: <b>%s</b>
💱 Метод оплаты: <b>Bitcoin</b>
➖➖
Для приобретения выбранного товара, оплатите:
➖➖
💸 <code>%s</code> BTC
➖➖
на Bitcoin кошелек:
<code>%s</code>
➖➖
#⃣ Заказ <b>№%s</b>, запомните его.
➖➖
Комментарий для проверки
💬 %s
➖➖
По номеру заказа вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства
➖➖
Купить Bitcoin можно через обменники, например 👉 здесь (http://www.bestchange.ru/qiwi-to-bitcoin.html).
➖➖
Для того, чтобы посмотреть последний Ваш заказ нажмите 👉 /lastorder
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_11_message = """🏠 Город: <b>%s</b>
🏃 Район: <b>%s</b>
🎁 Название: <b>%s</b>
💰 Стоимость: <b>%s</b>
💱 Метод оплаты: <b>Bitcoin</b>
➖➖
Для приобретения выбранного товара, оплатите:
➖➖
💸 <code>%s</code> LTC
➖➖
на Litecoin кошелек:
<code>%s</code>
➖➖
#⃣ Заказ <b>№%s</b>, запомните его.
➖➖
Комментарий для проверки
💬 %s
➖➖
По номеру заказа вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства
➖➖
Купить Litecoin можно через обменники, например 👉 здесь (http://www.bestchange.ru/qiwi-to-litecoin.html).
➖➖
Для того, чтобы посмотреть последний Ваш заказ нажмите 👉 /lastorder
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_2_message = """🏠 Город: <b>%s</b>
🏃 Район: <b>%s</b>
🎁 Название: <b>%s</b>
💰 Стоимость: <b>%s</b>
💱 Метод оплаты: <b>Банковская карта</b>
➖➖
Для приобретения выбранного товара, оплатите:
➖➖
💸 <code>%s</code> руб.
➖➖
на Банковскую карту:
<code>%s</code>
➖➖
#⃣ Заказ <b>№%s</b>, запомните его.
➖➖
Комментарий для проверки
💬 %s
➖➖
По номеру заказа вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства
➖➖➖➖
❗️ Реквизиты действительны в течении 30 минут!
➖➖
Для того, чтобы посмотреть последний Ваш заказ нажмите 👉 /lastorder
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_3_message = """🏠 Город: <b>%s</b>
🏃 Район: <b>%s</b>
🎁 Название: <b>%s</b>
💰 Стоимость: <b>%s</b>
💱 Метод оплаты: <b>SIM</b>
➖➖
Для приобретения выбранного товара, оплатите:
➖➖
💸 <code>%s</code> руб. (с коммиссия)
➖➖
на SIM:
<code>%s</code>
<code>%s</code>
➖➖
#⃣ Заказ <b>№%s</b>, запомните его.
➖➖
По номеру заказа вы сможете узнать статус заказа (получить адрес) в любой момент и с любого устройства
➖➖➖➖
❗️ Реквизиты действительны в течении 30 минут!
➖➖
Для того, чтобы посмотреть последний Ваш заказ нажмите 👉 /lastorder
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_4_message = """Произошла ошибка. Попробуйте еще раз.
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""
buy_5_message = """Недостаточно средств для оплаты заказа. Пополните баланс и попробуйте еще раз.
➖➖➖
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

buy_1_2_message = """❗️ Важно! Перед покупкой прочитайте мануал "Как купить Bitcoin за 15 секунд", нажмите на ссылку ниже:
➖➖➖➖
http://telegra.ph/Kak-kupit-Bitcoin-za-15-sekund-05-14-2
Чтобы вернуться в меню и начать сначала нажмите 👉 /start или @"""

start_3_message = """<b>Вас приветствует магазин - AmazonBIZ
Работай в AmazonBIZ на лучших условиях!



Нужные команды:</b>
/connect - выводит все доступные команды для связи с Администрацией
/myissues - последние 10 заявок по ненаходам
/myextickets - последние 10 зависших платежей на обменник

Удачных покупок!
➖
Привет, <b>%s</b>
Ваш баланс: 💰0 руб.
➖
Для пополнения баланса нажмите 👉/pay
Для просмотра баланса нажмите 👉/balance
Для просмотра истории операций по счету нажмите 👉 /history
Для получения информации о тикетах, перезакладах и зависших платежах нажмите 👉 /connect
➖
Для того чтобы узнать как проверять заказы нажмите 👉/check
➖
Для того чтобы посмотреть 10 последних отзывов о нашем магазине нажмите 👉/reviews
Для того чтобы добавить отзыв нажмите 👉/addreview
➖
Для управления персональными ботами нажмите 👉 /mybots
Для добавления персонального бота нажмите 👉 /addbot
Для получения информации о реферальной программе нажмите 👉 /ref
➖
Чтобы посмотреть список заявок на покупки или пополнения через SIM или банковскую карту нажмите 👉/trans
➖
Для получения помощи нажмите 👉 /help
Для просмотра последнего заказа нажмите 👉 /lastorder
➖
Выберите город:"""


# ОТЗЫВЫ О ТОВАРЕ
product_1_message = """🏃 Автор: D***********1
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Всё чётко, кура красавчик"""
product_2_message = """🏃 Автор: 5********4
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

На месте 👍"""
product_3_message = """🏃 Автор: 3*******1
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Изи катка в касание ,спасибо ,еще и камнем целом !!!"""
product_4_message = """🏃 Автор: 5********3
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

76753.спасибо в касание"""
product_5_message = """🏃 Автор: A******6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %a

Успешно """
product_6_message = """🏃 Автор: A*****a
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все четко кач бомба, подъем изи место антишкур. Но недавно брат ед. приехал забирать через сутки и не нашёл будто и не было.)"""
product_7_message = """🏃 Автор: b***4
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все ровно магаз четкий как всегда в касашку 
Кач мощный"""
product_8_message = """🏃 Автор: A**************o
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Дома.
Нашёл легко от души)
Можно просьбу (поменьше леса) ночью стрёмно идти за целью
А так став отменный."""
product_9_message = """🏃 Автор: A******6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Скатался на край света, удачно."""
product_10_message = """🏃 Автор: S*******3
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Балдеж малдеж"""
product_11_message = """🏃 Автор: J********7
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

10/10"""
product_12_message = """🏃 Автор: F********P
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

В подобных кладах необходимо дальний ракурс фото, а не просто ствол дерева. Кач 10/10"""
product_13_message = """🏃 Автор: G********6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все четко👌🏻"""
product_14_message = """🏃 Автор: B******f
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

км скинул напротив места где сидят и отдыхают люди, потратил полтора часа своего времени на снятие, неприятно. Вес норм, кач топ."""
product_15_message = """🏃 Автор: S*************7
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Чётко, точно, близко!! Красивая работа👍"""
product_16_message = """🏃 Автор: T*************i
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Забрал.все четко, все дома."""
product_17_message = """🏃 Автор: T************2
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Всё норм в касание"""
product_18_message = """🏃 Автор: 2*******2
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

В касание! Красавцы пацаны. Жду купон!"""
product_19_message = """🏃 Автор: 7*******2
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все в поряде👍 В касание🔥 Может порадуете купончиком?)"""
product_20_message = """🏃 Автор: 1********0
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Всё прошло успешно. Спасибо"""
product_21_message = """🏃 Автор: 5********6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все на месте. Продолжай в том же духе. Стаф хороший"""
product_22_message = """🏃 Автор: L********1
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Чуть чуть не по метке. Съём очень лёгкий, кач хороший."""
product_23_message = """🏃 Автор: 7*******2
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

В касание"""
product_24_message = """🏃 Автор: A*******o
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Всем привет магазин хороший, всё устраивает, цена и стаф, за всё время было пару ненаходов и то по мелочевке!"""
product_25_message = """🏃 Автор: d************o
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Все четко"""
product_26_message = """🏃 Автор: 5********6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Дома )еще не пробовал но в качестве не сомневаюсь"""
product_27_message = """🏃 Автор: 4*******3
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

В касание,побольше таких кладов."""
product_28_message = """🏃 Автор: 6********3
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Нашёл. Брал прикоп, а в итоге клад висел на ветках травы."""
product_29_message = """🏃 Автор: x************7
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Всё гуд!"""
product_30_message = """🏃 Автор: A******6
🍕 Товар: %s
📆 Дата: %s
📊 Оценка: %s

Место кайфовое, безлюдное, съем легчайший.🤝"""


MESSAGES = {
    "start": start_message,
    "start_2": start_2_message,
    "start_3": start_3_message,

    "not_command": not_command_message,
    "poll": poll_message,
    "ref": ref_message,
    "balance": balance_message,
    "check": check_message,
    "help": help_message,
    "connect": connect_message,
    "history": history_message,
    "addreview": addreview_message,
    "lastorder": lastorder_message,
    "issue": issue_message,
    "myissues": myissues_message,

    "captha": captha_message,

    "pay": pay_message,
    "pay1_1": pay1_1_message,
    "pay5_1": pay1_1_message,
    "pay1_2": pay1_2_message,
    "pay5_2": pay5_2_message,
    "pay2_1": pay2_1_message,
    "pay2_2": pay2_2_message,
    "pay3_1": pay3_1_message,
    "pay3_2": pay2_2_message,
    "pay4_1": pay4_1_message,
    "not_count": not_count_message,
    "min_count": min_count_message,
    "not_coupon": not_coupon_message,
    "pay1_what_pay": pay1_what_pay_message,
    "pay5_what_pay": pay5_what_pay_message,
    "pay2_what_pay": pay2_what_pay_message,
    "pay1_3": pay1_3_message,
    "pay5_3": pay5_3_message,
    "pay2_3": pay2_3_message,
    "pay3_3": pay2_3_message,

    "trans_non": trans_non_message,
    "trans": trans_message,
    "reviews1": reviews1_message,
    "reviews2": reviews2_message,
    "reviews3": reviews3_message,

    "addbot": addbot_message,
    "success_add_bot": success_add_bot_message,
    "error_add_bot": error_add_bot_message,
    "there_is_bot": there_is_bot_message,
    "not_my_bots": not_my_bots_message,
    "my_bot_1": my_bot_1_message,
    "my_bot_2": my_bot_2_message,
    "exticket": exticket_message,
    "success_exticket": success_exticket_message,
    "not_exticket": not_exticket_message,
    "error_exticket": error_exticket_messsage,
    "not_photo": not_photo_message,
    "success_photo": success_photo_message,
    "exticket_send": exticket_send_message,
    "exticket_in": exticket_in_message,
    "not_myexticket": not_myexticket_message,
    "not_myextickets": not_myextickets_message,
    "removebot": removebot_message,
    "not_removebot": not_removebot_message,
    "success_removebot": success_removebot_message,

    "not_city": not_city_message,
    "buy_product": buy_product_message,
    "buy_1": buy_1_message,
    "buy_11": buy_11_message,
    "buy_2": buy_2_message,
    "buy_3": buy_3_message,
    "buy_4": buy_4_message,
    "buy_5": buy_5_message,

    "buy_1_2": buy_1_2_message,


    "product_1": product_1_message,
    "product_2": product_2_message,
    "product_3": product_3_message,
    "product_4": product_4_message,
    "product_5": product_5_message,
    "product_6": product_6_message,
    "product_7": product_7_message,
    "product_8": product_8_message,
    "product_9": product_9_message,
    "product_10": product_10_message,
    "product_11": product_11_message,
    "product_12": product_12_message,
    "product_13": product_13_message,
    "product_14": product_14_message,
    "product_15": product_15_message,
    "product_16": product_16_message,
    "product_17": product_17_message,
    "product_18": product_18_message,
    "product_19": product_19_message,
    "product_20": product_20_message,
    "product_21": product_21_message,
    "product_22": product_22_message,
    "product_23": product_23_message,
    "product_24": product_24_message,
    "product_25": product_25_message,
    "product_26": product_26_message,
    "product_27": product_27_message,
    "product_28": product_28_message,
    "product_29": product_29_message,
    "product_30": product_30_message,
}
