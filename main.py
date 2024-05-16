from colorama import init, Fore
from random import choice
from datetime import datetime
from time import sleep

filename = f"dialogs\dialog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

init()  # Ініціалізація модуля Colorama


def get_user_input():  # Функція записує вхідні дані у файл та повертає відформатоване введення даних
    user_input = input(Fore.LIGHTWHITE_EX + f'[{name_user}]: ').lower()
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(f'[{name_user}]: {user_input}\n')
    return user_input


def print_write(text):  # Функція виконує дві дії поступово: виводить текст боту та повертає запис тексту у файл
    with open(filename, 'a', encoding="utf-8") as f:  # Відкриття текстового файлу для запису
        print(Fore.LIGHTBLUE_EX + text)
        return f.write(f'{text}\n')


def random_phrase():  # Функція повертає випадкову фразу помилки введення даних
    phrases = ['Я такого не можу зрозуміти. Спробуй ще раз.', 'Я гадаю, що відповіді на це питання в мене немає',
               "Дуже класна тема, в наступній версії обов'язково додам.",
               'Я не настільки розумний, щоб знайти відповідь на це запитання.',
               'Щось не виходить, спробуй ще раз.', 'Відповіді на це питання я не маю, вибач.']
    return choice(phrases)


def physics():  # Функція "Фізика" виконує відповіді на конкретні запитання теми
    print_write(f'''{name_bot}: Ви обрали тему "Фізика".
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) Рівняння Гейзенберга невизначеності (рівняння)
          2) Закон Стефана-Больцмана (закон)
          3) Кулонівська стала (стала)
          4) Повернутись назад (назад)
          5)    ВИХІД''')

    topic = get_user_input()  # Вибір теми предмету
    sleep(short)  # Затримка виведення коду через модуль time

    if topic in ['рівняння', '1']:  # Маємо два варіанти введення на вибір - скорочене визначення або номер теми
        print_write(f'{name_bot}: Δx×Δp >= h (Стала Планка h = 6,626 070 15 × 10^-34 Дж/с)')

        try:  # Конструкція для перевірки на помилку ValueError
            x = float(input(f'{name_bot}: Похибка вимірювання положення частинки Δx = '))
            p = float(input(f'{name_bot}: Похибка вимірювання положення її імпульсу Δp = '))
            print_write(f'{name_bot}: Відповідь: {["Невірно", "Все вірно"][x * p >= 6.626_070_15 * 10 ** -34]}')
            sleep(long)
            return physics()
        except ValueError:
            # Помилка завжди різна в залежності від теми питання
            print_write(f'{name_bot}: Похибка має бути дійсним числом. Спробуйте ще раз.')
            sleep(short)
            return physics()

    elif topic in ['закон', '2']:
        print_write(f'{name_bot}: R = σ×A×T^4(Стала Больцмана σ = 5,67 × 10^-8 Вт/м²K^4)')
        try:
            t = float(input(f'{name_bot}: Абсолютна температура тіла T = '))
            a = float(input(f'{name_bot}: Площа поверхні тіла A = '))
            print_write(f'{name_bot}: Відповідь: P = {5.67 * 10 ** -8 * a * t ** 4}')
            sleep(long)
            return physics()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Дані мають бути дійсним числом. Спробуйте ще раз.')
            sleep(short)
            return physics()

    elif topic in ['стала', '3']:
        print_write(f'{name_bot}: Кулонівська стала: 9 × 10^9 Н×м²/Кл²')
        sleep(long)
        return physics()

    elif topic in ['назад', '4']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '5']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(physics)

    else:  # Якщо введені дані не вдається розпізнати - відбувається виклик повернення до початкової функції (Фізика)
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return physics()


def math():
    print_write(f'''{name_bot}: Ви обрали тему "Математика".
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) Формула для обчислення відстані між двома точками в просторі (формула)
          2) Площа прямокутника (прямокутник)
          3) Площа трапеції (трапеція)
          4) Рівняння кола (рівняння)          
          5) Повернутись назад (назад)
          6)    ВИХІД''')

    topic = get_user_input()
    sleep(short)

    if topic in ['формула', '1']:
        print_write(f'{name_bot}: d = √((x2 - x1)² + (y2 - y1)² + (z2 - z1)²)')
        try:
            x1, y1, z1 = map(int,
                             input(f'{name_bot}: Введіть координати першої точки через пробіл (x1 y1 z1) = ').split())
            x2, y2, z2 = map(int,
                             input(f'{name_bot}: Введіть координати другої точки через пробіл (x2 y2 z2) = ').split())
            print_write(f'{name_bot}: Відповідь: d = {((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5}')
            sleep(long)
            return math()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Координати мають бути цілим числом. Спробуйте ще раз.')
            sleep(short)
            return math()

    elif topic in ['прямокутник', '2']:
        print_write(f'{name_bot}: S = a × b')
        try:
            a = float(input(f'{name_bot}: Перша сторона прямокутника а = '))
            b = float(input(f'{name_bot}: Друга сторона прямокутника b = '))
            print_write(f'{name_bot}: Відповідь: S = {a * b}')
            sleep(long)
            return math()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Сторони мають бути цілим числом. Спробуйте ще раз.')
            sleep(short)
            return math()

    elif topic in ['трапеція', '3']:
        print_write(f'{name_bot}: S = 1/2 × (a + b) × h')
        try:
            a = float(input(f'{name_bot}: Перша сторона трапеції а = '))
            b = float(input(f'{name_bot}: Друга сторона трапеції b = '))
            h = float(input(f'{name_bot}: Висота трапеції h = '))
            print_write(f'{name_bot}: Відповідь: S = {0.5 * (a + b) * h}')
            sleep(long)
            return math()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Сторони мають бути цілим числом. Спробуйте ще раз.')
            sleep(short)
            return math()

    elif topic in ['рівняння', '4']:
        print_write(f'{name_bot}: Рівняння має вигляд - (x - a)² + (y - b)² = R²')
        try:
            a = int(input(f'{name_bot}: Координата центру кола Ox, а = '))
            b = int(input(f'{name_bot}: Координата центру кола Oy, b = '))
            r = int(input(f'{name_bot}: Радіус кола Oy, R = '))
            print_write(f'{name_bot}: Відповідь: (x - {a})² + (y - {b})² = {r ** 2}')
            sleep(long)
            return math()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Координати мають бути цілим числом. Спробуйте ще раз.')
            sleep(short)
            return math()

    elif topic in ['назад', '5']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '6']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(math)

    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return math()


def geography():
    print_write(f'''{name_bot}: Ви обрали тему "Географія".  
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) 5 найвищих гір у світі (гори)
          2) Найбільший материк за площею (материк)
          3) Країна, в якій знаходиться найбільша пустеля після Сахари (пустеля)
          4) Відстань між двома точками на площині (відстань)
          5) Повернутись назад (назад)
          6)    ВИХІД''')

    topic = get_user_input()
    sleep(short)

    if topic in ['гори', '1']:
        print_write(f'''{name_bot}: 5 найвищих гір у світі:
          1) Еверест (Махалангур-Гімал, Гімалаї) - 8849м.
          2) К2 (Балторо-Музтаг, Каракорум) - 8611м.
          3) Канченджанґа (Канченджанґа, Гімалаї) - 8586м.
          4) Лхоцзе (Махалангур-Гімал, Гімалаї) - 8516м.
          5) Макалу (Махалангур-Гімал, Гімалаї) - 8485м''')
        sleep(long)
        return geography()

    elif topic in ['материк', '2']:
        print_write(f'''{name_bot}: Найбільшим материком за площею у світі вважають Євразію.
          Материк займає близько 55 000 000 км², або близько 36,2 % загальної площі суходолу Землі.''')
        sleep(long)
        return geography()

    elif topic in ['пустеля', '3']:
        print_write(f'''{name_bot}: Країна, в якій знаходиться найбільша пустеля після Сахари є
          Аравійська пустеля: батьківщина бедуїнів.
          Розташування: Аравійський півострів.
          Площа: 2,3 млн км².
          Середня температура: взимку близько +10 °C, влітку близько +45 °C.''')
        sleep(long)
        return geography()

    elif topic in ['відстань', '4']:
        print_write(f'{name_bot}: Відстань між двома точками на площині: d = √((x2 - x1)² + (y2 - y1)²)')
        try:
            x1, y1 = map(int, input(f'{name_bot}: Введіть координати першої точки через пробіл (x1 y1) = ').split())
            x2, y2 = map(int, input(f'{name_bot}: Введіть координати другої точки через пробіл (x2 y2) = ').split())
            print_write(f'{name_bot}: Відповідь: d = {((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5}')
            sleep(long)
            return geography()
        except ValueError:
            print_write(f'{name_bot}: Помилка. Координати мають бути цілим числом. Спробуйте ще раз.')
            sleep(short)
            return geography()

    elif topic in ['назад', '5']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '6']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(geography)

    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return geography()


def philology():
    print_write(f'''{name_bot}: Ви обрали тему "Філологія".
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) Як утворюються питальні речення в англійській мові? (речення)
          2) Яка різниця між іменником та прикметником? (різниця)
          3) Як утворити форму множини іменників в українській мові? (форма)
          4) Повернутись назад (назад)
          5)    ВИХІД''')

    topic = get_user_input()
    sleep(short)

    if topic in ['речення', '1']:
        print_write(f'''{name_bot}: Утворення питальних речень в англійській мові:
          Питальне слово + допоміжне (або модальне)
          дієслово + підмет + присудок + додаток + інші члени речення.
          Простіше — на прикладі: What (питальне слово) are (допоміжне дієслово)
          you (підмет) cooking (присудок)? – Що ти готуєш?
          Докладніше за посиланням: https://www.englishdom.com/ua/blog/vidi-pitan-v-anglijskij/''')
        sleep(long)
        return philology()

    elif topic in ['різниця', '2']:
        print_write(f'''{name_bot}: Різниця між іменником та прикметником:
          1) Іменник називає предмет, явище або стан. Прикметник називає їх ознаку.
          2) Іменник відповідає на питання хто? що?
             Звязок іменників з прикметниками визначається з питань який? яка? яке?
          3) Прикметник, на відміну від іменника, не володіє категорією одухотвореності / бездушності.
             Докладніше за посиланням:
        https://www.avktarget.com/articles/nauka-i-obrazovanie/raznica-mezhdu-prilagatelnim-i-sushestvitelnim.html''')
        sleep(long)
        return philology()

    elif topic in ['форма', '3']:
        print_write(f'''{name_bot}: Утворення форми множини іменників в українській мові:
          Іменники середнього роду мають у називному і знахідному відмінках множини закінчення -а або -я 
          (озеро-озера, море-моря). Іменники жіночого роду мають закінчення -а або -і (дівчина-дівчата, радість-радості) 
          Іменники чоловічого роду мають закінчення -и або -і (вітер-вітри, кінь-коні).''')
        sleep(long)
        return philology()

    elif topic in ['назад', '4']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '5']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(philology)

    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return philology()


def astronomy():
    print_write(f'''{name_bot}: Ви обрали тему "Астрономія".
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) Яка є відстань між Землею та Сонцем? (відстань)
          2) Що таке чорні діри та як вони виникають? (діри)
          3) Повернутись назад (назад)
          4)    ВИХІД''')

    topic = get_user_input()
    sleep(short)

    if topic in ['відстань', '1']:
        print_write(f'''{name_bot}: В середньому відстань від Землі до Сонця становить 92 955 807 миль (149 577 870 км). 
          Відстань від Землі до Сонця називається астрономічною одиницею, або а.о. 
          і використовується для вимірювання відстаней у всій Сонячній системі. ''')
        sleep(long)
        return astronomy()

    elif topic in ['діри', '2']:
        print_write(f'''{name_bot}: Чорна діра – це місце в космосі, куди сила тяжіння затягує настільки сильно, 
          що навіть світло не може чинити опір. Сила тяжіння там настільки сильна, тому що речовина 
          була стиснута в крихітний простір. Чорна діра може виникнути, коли зірка вмирає. 
          Оскільки світло не виходить, люди не можуть бачити чорні діри.''')
        sleep(long)
        return astronomy()

    elif topic in ['назад', '3']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '4']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(astronomy)

    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return astronomy()


def general():
    print_write(f'''{name_bot}: Ви обрали тему "Загальні".
{name_bot}: Ви можете задати мені питання з наступних тем:
{name_bot}: 1) Яка зараз пора року? (пора року)
          2) Як мене звати? (бот)
          3) Заспівати колядку? (колядка)
          4) Яку першу іграшку рекламували по телебаченню? (іграшка)
          5) Як спочатку називався Нью-Йорк? (нью-йорк)
          6) Скільки тривала Столітня війна? (війна)
          7) Яка рослина квітне лише в народних легендах? (рослина)
          8) Де знаходиться найсухіше місце на Землі? (місце)
          9) Скільки бактерій живе в організмі людини? (бактерії)
          10) Повернутись назад (назад)
          11)    ВИХІД''')

    topic = get_user_input()
    sleep(short)

    if topic in ['пора року', '1']:
        seasons = {(1, 2, 12): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Літо', (9, 10, 11): 'Осінь'}

        for i in seasons:  # Перебір ключів (кортежів) в словнику seasons
            if datetime.timetuple(datetime.now())[1] in i:  # 1-ий індекс в кортежі timetuple(2023, 05, 01) - це 5
                season = seasons[i]  # 5 знаходиться в ключі (3, 4, 5) зі значенням Весна
                break  # Тому привласнюємо це значення змінній season

        print_write(f'''{name_bot}: Зараз: {datetime.now().strftime('%H:%M:%S %Y-%m-%d')}.
          Пора року: {season}.''')
        sleep(long)
        return general()

    elif topic in ['бот', '2']:
        print_write(f'Мене звати {name_bot}. Ви напевно забули, що ми на початку вітались).')
        sleep(short)
        return general()

    elif topic in ['колядка', '3']:
        print_write(f'''{name_bot}: Колядки – це обрядові пісні, які діти співають для дорослих. 
          У цих віршах вони бажають здоров'я господарям та отримують натомість гостинці.
          Оберіть варіант колядки від 1 до 3.''')

        num_poem = get_user_input()
        sleep(short)

        if num_poem == '1':
            print_write(f'''{name_bot}: Коляд, коляд, колядниця,
          Добра з медом паляниця,
          А без меду не така,
          Дайте, дядьку, п’ятака.
          Одчиняйте скриньку,
          Та давайте сливку,
          Одчиняйте сундучок,
          Та давайте п’ятачок.''')
            sleep(long)
            return general()

        elif num_poem == '2':
            print_write(f'''{name_bot}: Нова радість стала, яка не бувала,
          Над вертепом звізда ясна світлом засіяла.
          Де Христос родився, з Діви воплотився,
          Як чоловік пеленами убого оповився.
          Пастушки з ягнятком перед тим дитятком
          На колінця припадають, Царя-Бога вихваляють.
          – Ой ти, Царю, Царю, небесний Владарю,
          Даруй літа щасливії цього дому господарю.
          Даруй господарю, даруй господині,
          Даруй літа щасливії нашій славній Україні.''')
            sleep(long)
            return general()

        elif num_poem == '3':
            print_write(f'''{name_bot}: Коляд, коляд ,коляда
          У віконце загляда.
          У різдвяну світлу нічку
          Запали на радість свічку.
          Коляду поклич до хати,
          Щоб Ісуса привітати.
          Люди добрі, колядуйте,
          Сина Божого шануйте!''')
            sleep(long)
            return general()

        else:
            print_write(f'{name_bot}:{random_phrase()}')
            sleep(short)
            return general()

    elif topic in ['іграшка', '4']:
        print_write(f'''{name_bot}: Пан Картопляна Голова.
          Mr. Potato Head була вперше створена в 1952 році компанією, яка згодом стала відомою як Hasbro, Inc. 
          30 квітня того ж року іграшка з'явилася в першій рекламі, яка була орієнтована на дітей, а не на дорослих.''')
        sleep(long)
        return general()

    elif topic in ['нью-йорк', '5']:
        print_write(f'''{name_bot}: Новий Амстердам.
          Новий Амстердам був голландським поселенням 17-го століття, заснованим на південному краю острова Манхеттен. 
          У 1664 році англійці захопили Новий Амстердам і перейменували його в Нью-Йорк на честь герцога Йоркського''')
        sleep(long)
        return general()

    elif topic in ['війна', '6']:
        print_write(f'''{name_bot}: 116 років.
          Столітня війна, конфлікт між Англією та Францією, фактично тривала 116 років. 
          Він почався в 1337 році і закінчилося в 1453 році, 
          хоча в цей час були тривалі періоди перемир'я або бойових дій на низькому рівні.''')
        sleep(long)
        return general()

    elif topic in ['рослина', '7']:
        print_write(f'''{name_bot}: Папороть. 
          Згідно з фольклором вона цвіла лише одну мить. Знайти її міг лише молодик. 
          За деякими легендами, неодмінно неодружений і єдиний син у сім'ї. 
          Квітка папороті символізувала енергію сонця, відродження життя, розквіт почуттів.''')
        sleep(long)
        return general()

    elif topic in ['місце', '8']:
        print_write(f'''{name_bot}: Найсухіше місце на Землі знаходиться в Антарктиді. 
          Хоч як дивно це звучить, але деякі ділянки антарктичної долини 
          Мак-Мердо не бачили опадів уже 2 мільйона років.''')
        sleep(long)
        return general()

    elif topic in ['бактерії', '9']:
        print_write(f'''{name_bot}: На одну клітину людського тіла припадає десять мікроорганізмів. 
          У тілі однієї людини живе сотня трильйонів бактерій. 
          Мікроорганізми становлять від 1-го до 3-х відсотків маси тіла людини. 
          Тобто людина вагою 90 кілограмів має в собі 3 кілограми бактерій.''')
        sleep(long)
        return general()

    elif topic in ['назад', '10']:
        print_write(f'{name_bot}: Повертаємось до списку предметів...')
        sleep(short)
        return choose_subjects()()

    elif topic in ['вихід', '11']:
        sleep(short)
        return goodbye()

    elif topic == 'допоможи':
        sleep(short)
        return instruction(general)

    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return general()


def goodbye():
    print_write(f'{name_bot}: Дякую за спілкування. Гарного дня, {name_user}.')
    sleep(long)


# todo add func to Dictionary
def choose_subjects():
    print_write(f'''{name_bot}: Добре, {name_user}.
{name_bot}: Ви в будь-який момент можете написати команду "Допоможи" і дізнаєтесь як працювати зі мною. 
{name_bot}: Задайте мені питання з наступних предметів:
{name_bot}: Фізика, Математика, Географія, Філологія, Астрономія, Загальні.''')

    subject = get_user_input()  # Вибір предмету для наступних запитань
    sleep(short)  # Затримка виведення програми

    if subject in ['фізика', 'математика', 'географія', 'філологія', 'астрономія', 'загальні', 'допоможи', 'вихід']:
        # Словник з ключами у вигляді переліку предметів та значень у вигляді виклику функцій
        return {'фізика': physics, 'математика': math,
                'географія': geography, 'філологія': philology,
                'астрономія': astronomy, 'загальні': general,
                'допоможи': instruction, 'вихід': goodbye}.get(subject)
    else:
        print_write(f'{name_bot}: {random_phrase()}')
        sleep(short)
        return choose_subjects()()  # Спробуй ще раз


def instruction(subject=None):  # Функція допомоги користувачу
    print_write(f'{name_bot}: Зараз у всьому розберемось {name_user}...')
    sleep(short)

    print_write(f'''{name_bot}: 1) Регістр вхідних даних неважливий!
          2) Я використовую деякий час затримки виводу інформації для того, 
             щоб ви змогли краще ознайомитись з відповіддю на ваше запитання або помилкою під роботи.
          3) Ви маєте два варіанти для вибору запитання по темі предмету:
             Наприклад: *1*) Рівняння Гейзенберга невизначеності (*рівняння*)
             У даному випадку ви можете написати або "1" або "Рівняння" - в обох випадках я вас зрозумію.
          4) Якщо ви хочете закінчити спілкування -  напишіть "Вихід" у будь-який момент.
          5) Якщо ви обрали не той предмет та хочете повернутись до головного меню - напишіть "Назад".''')
    sleep(long)

    print_write(f'{name_bot}: Можемо продовжувати?')
    answer = get_user_input()
    while answer not in ['так', 'да', '+', 'звісно']:
        print_write(f'{name_bot}: Добре, я почекаю...')
        sleep(long)
        print_write(f'{name_bot}: Можемо продовжувати?')
        answer = get_user_input()
    if subject:
        return subject()
    else:
        return choose_subjects()()


# Змінні затримки в секундах
short = 1.5
long = 5

name_bot = '[HELPER]'  # Форматування тексту боту під колір
print_write(f'''[Bot]: Вітаю, мене звати {name_bot}.
{name_bot}: Я буду вам допомагати у вирішенні складних питань.
{name_bot}: Як можна до вас звертатись?''')
name_user = input(Fore.LIGHTWHITE_EX + '[User]: ')
with open(filename, 'a', encoding="utf-8") as file:
    file.write(f'[User]: {name_user}\n')
sleep(short)
choose_subjects()()
