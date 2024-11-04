# -*- coding: utf-8 -*-
"""

Running in Tim Industries

Created on Mon Nov  4 15:55:24 2024
in Tims II Lab

@author: Stark
"""


from parser import HomeMephiParser

from bs4 import BeautifulSoup as bs
import re


hmp = HomeMephiParser()

q = '''<!DOCTYPE html>
<html lang='ru'>
<head>
<title>Григорьев А.А. — НИЯУ МИФИ</title>

<meta charset='utf-8'>
<meta content='#28828a' name='theme-color'>
<meta content='IE=edge' http-equiv='X-UA-Compatible'>
<meta content='width=device-width, initial-scale=1.0' name='viewport'>
<link rel="stylesheet" media="all" href="/assets/application-5fce1f02c2ee6c0fa68ed741f5ee9d2eb7c7bec60ad0e10d0ba06673034c8437.css" data-turbolinks-track="true" />
<script src="/assets/application-31e4860891c96e3da4ef6bc2e3cf5da04c514dc1274b73120536bd4cd98e4164.js" data-turbolinks-track="true"></script>
<script src="https://api-maps.yandex.ru/2.1/?apikey=73472fad-e902-42a2-b833-77bdd0b03fa4&amp;lang=ru_RU" data-turbolinks-track="reload"></script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="aC9a2W/vdqFLrF72h8U/viGBIDf5yEjQsXyESPgnjvzx65qXvJnm23t/SW0QdNLRTz4irRr9DEdnV+jKlvKCFA==" />
<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-ccc17adba7d1cab56b722a44ba17833da4c07ece563e2159341a8408c88e16f9.ico" />
<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-32x32-f4c75b262b102802b0ae2b746117e22c230256f2eb412a95ad1e6654fcc1daac.png" sizes="32x32" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-icon-bdb1d36704f3c6227ebf76bcf5f8b2964f5ae5bd86d39622d2b2c3175938f0b8.png" />
<script>
  (function() {
    window.authorized = 1;
  
  }).call(this);
</script>

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({tex2jax: {inlineMath: [ ['$','$'] ]}});
</script>
<script src="/mathjax/MathJax.js?config=TeX-AMS_HTML-full.js" type="text/javascript"></script>
<script src='https://yastatic.net/es5-shims/0.0.2/es5-shims.min.js'></script>
<script src='https://yastatic.net/share2/share.js'></script>
<script src="https://www.gstatic.com/charts/loader.js"></script>
</head>
<body data-id='26773'>
<div id='wrapper'>
<aside id='sidebar-wrapper'>
<ul class='sidebar-nav'>
<li class='sidebar-brand'>
<a href="/"><img alt="НИЯУ МИФИ" src="/assets/mephi_logo_small_white-49172193011e57532a72d6e713f177ccd81eb0cd80bb6274eb315d922936bf41.png" />
</a></li>
<li>
<a href="/users/26773"><i class="fa fa-home fa-fw"></i>
Личная страница
</a></li>
<li>
<a href="/talks"><i class="fa fa-envelope fa-fw"></i>
Сообщения
<span class='count_unread_talks pull-right badge'>23</span>
</a></li>
<li>
<a href="/bookmarks"><i class="fa fa-bookmark fa-fw"></i>
Сервисы
</a></li>
<li>
<a href="/users"><i class="fa fa-user fa-fw"></i>
Пользователи
</a></li>
<li>
<a href="/notifications"><i class="fa fa-bell fa-fw"></i>
Уведомления
<span class='count_unread_notifications pull-right badge'>37</span>
</a></li>
<li>
<a href="/users/26773/members"><i class="fa fa-users fa-fw"></i>
Сообщества
</a></li>
<li>
<a href="/events"><i class="fa fa-calendar fa-fw"></i>
Мероприятия
</a></li>
<li>
<a href="/study_groups"><i class="fa fa-clock-o fa-fw"></i>
Расписание
</a></li>
<li>
<a href="/contests/1"><i class="fa fa-rocket fa-fw"></i>
Конкурс «Студент года»
</a></li>
<li>
<a target="_blank" href="https://mycareer.mephi.ru"><i class="fa fa-briefcase fa-fw"></i>
Старт карьеры. <br/> Шоу-рум работодателей
</a></li>
<li>
<a href="/app"><i class="fa fa-mobile fa-fw"></i>
Мобильное приложение
</a></li>
<li>
<a href="/telegram"><i class="fa fa-telegram fa-fw"></i>
Telegram-бот
</a></li>
<li>
<a href="/development_program"><i class="fa fa-line-chart"></i>
Программа развития
</a></li>
<li>
<a href="/logout"><i class="fa fa-sign-out fa-fw"></i>
Выход
</a></li>
</ul>
</aside>

<nav class='navbar navbar-rosatom m-b-0'>
<a target="_blank" class="navbar-brand" href="https://fb-portal.com/survey-new/ec7f2d9e16d875a21d42aa8cd2286286">Поделитесь вашем мнением об учебе и жизни в университете! Пройти опрос
</a></nav>
<nav class='navbar navbar-inverse'>
<div class='container-fluid'>
<a id="sidebar-toggle" class="navbar-text" href="#wrapper"><i class="fa fa-bars"></i>
</a><div class='navbar-header'>
<a class="navbar-brand" href="/">Корпоративный портал
</a></div>
<ul class='nav navbar-nav navbar-right'>
<li class='dropdown'>
<a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="fa fa-circle user-online-status user_26773 user-online"></i>
<span class='hidden-xs'>Андреев Т.П.</span>
<div class="user-avatar user-tiny hidden-xs"><img alt="Андреев Т.П." class="user-responsive" src="/system/users/avatars/000/026/773/tiny/fotodok_%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F.jpg?1662014109" /></div>
<i class="fa fa-angle-down"></i>
</a><ul class='dropdown-menu'>
<li>
<a href="/logout"><i class="fa fa-sign-out fa-fw"></i>
Выход
</a></li>
</ul>
</li>
</ul>
</div>
</nav>


<div id='page-content-wrapper'>
<div class='container-fluid'>


<div class='row'>
<div class='col-md-4'>
<div class='box'>
<div class='text-center'>
<div class="user-avatar user-medium user-center"><a href="/users/32708"><img alt="Григорьев А.А." class="user-responsive" src="/system/users/avatars/000/032/708/medium/photo1699886487.jpeg?1710319111" /></a></div>
</div>
<h3 class='text-center light'>
<i class="fa fa-circle user-online-status user_32708 user-offline"></i>
<span title='aagrigorev1'>Григорьев</span>
<br>
Андрей
Александрович
</h3>
<div class='text-center'>
<a class="btn btn-primary wrap" href="/talks/new?user_id=32708"><i class="fa fa-envelope"></i>
Отправить сообщение
</a></div>
<div>
<div class='pull-right'>
</div>
<div>Работает в МИФИ с 2019 года</div>
<ul class='list-inline text-center'>
<li><a title="Telegram" target="_blank" href="https://t.me/grigandal"><i class="fa fa-telegram"></i></a></li>
</ul>
<a class="btn btn-outline btn-primary btn-xs pull-right link_to_scroll visible-xs visible-sm" href="#schedules_wrapper"><i class="fa fa-calendar"></i>
Расписание
</a><div class='clearfix'></div>
</div>
</div>

<h3 class='light'>Должности</h3>
<div class='list-group'>
<div class='list-group-item'>
Ассистент
<div class='text-muted'>
<small>Кафедра кибернетики (№22) института интеллектуальных кибернетических систем НИЯУ МИФИ</small>
</div>
</div>
</div>
<h3 class='light'>
Образование
</h3>
<div class='list-group'>
<div class='list-group-item'>Высшее образование — специалитет, магистратура: ФГАОУ ВО &quot;Национальный исследовательский ядерный университет &quot;МИФИ&quot;. 2022. Направление «Программная инженерия». Kвалификация «Магистр».  Диплом 107731 №0404568.</div>
</div>

<h3 class='light'>Преподаваемые дисциплины</h3>
<div class='list-group'>
<div class='list-group-item'>
<div>
<b>1.</b>
Введение в интеллектуальные системы и технологии
</div>
<div>
<b>2.</b>
Основы моделирования систем
</div>
</div>
</div>


</div>
<div class='col-md-8'>
<div id='schedules_wrapper'>
<div id='tutors_wrapper'><div class='box'>
<div>
<div class='btn-group'>
<a class="btn btn-primary btn-outline" href="/tutors/28390">Осень 2024. Расписание
</a><button name="button" type="button" class="btn btn-primary btn-outline dropdown-toggle dropdown-toggle-split" data-toggle="dropdown"><i class="fa fa-angle-down"></i></button>
<ul class='dropdown-menu'>
<li>
<a href="/tutors/28390.pdf"><i class="fa fa-print"></i>
PDF
</a></li>
<li>
<a href="/tutors/28390.ics"><i class="fa fa-calendar"></i>
ICS
</a></li>
</ul>
</div>
</div>
<div>
<h3 class='lesson-wday'>
<div class='pull-left'>
<a data-remote="true" href="/users/32708?offset=-1"><i class="fa fa-chevron-left"></i>
</a></div>
<div class='pull-right'>
<a data-remote="true" href="/users/32708?offset=1"><i class="fa fa-chevron-right"></i>
</a></div>
</h3>
<h4 class='text-center text-black text-uppercase text-muted'>понедельник, 04 ноября 2024</h4>
<div class='clearfix'></div>

<div class='alert alert-info'>Занятий не найдено</div>
</div>

</div>
</div>
<div id='students_wrapper'></div>
</div>

<div class='row'>
<div class='col-lg-6'>
</div>
<div class='col-lg-6'>
<div class='panel panel-counter panel-citations'>
<div class='panel-body'>
Среднее число цитирований статей (Scopus)
<div class='text-sm'>за последние 3 года</div>
<h3 class='count'>1.33</h3>
</div>
</div>
</div>
</div>
<div class='box'>
<h3 class='light'>Публикационная активность</h3>
<div class='panel-group' id='articles_panel' role='tablist'>
<div class='panel panel-default'>
<div class='panel-heading' id='user_other_articles' role='tab'>
<h4 class='panel-title'>
<a data-toggle="collapse" data-parent="#articles_panel" role="button" aria-expanded="true" aria-controls="user_other_articles_collapse" href="#user_articles_collapse">Публикации
</a></h4>
</div>
<div class='panel-collapse collapse panel-body' id='user_articles_collapse' role='tabpanel'>
<p class='text-muted'>Показаны публикации за последние 3 года</p>
<ol>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=68529226">ОСОБЕННОСТИ РАЗРАБОТКИ И ПРИМЕНЕНИЯ ОБУЧАЮЩИХ ИНТЕГРИРОВАННЫХ ЭКСПЕРТНЫХ СИСТЕМ ДЛЯ УЧЕБНОГО ПРОЕКТИРОВАНИЯ ДИНАМИЧЕСКИХ ИНТЕЛЛЕКТУАЛЬНЫХ СИСТЕМ РАЗЛИЧНОЙ АРХИТЕКТУРНОЙ ТИПОЛОГИИ</a>
//
Гибридные и синергетические интеллектуальные системы, 2024г.
<span class='text-muted'>

</span>
Стр. 240-251
</li>
<li><span class='label label-primary'>
Статья
</span>
<div class='label label-mint'>Web of Science &amp; Scopus</div>

<a target="_blank" href="https://www.doi.org/10.1109/Inforino60363.2024.10551996">Educational Design of Dynamic Intelligent System Prototypes Using Tutoring Integrated Expert Systems</a>
//
2024 7th International Conference on Information Technologies in Engineering Education, Inforino 2024 - Proceedings, 2024
<span class='text-muted'>
TOP10
</span>

<small>
<a target="_blank" class="text-nowrap" href="http://doi.org/10.1109/Inforino60363.2024.10551996">doi
<i class="fa fa-share"></i>
</a></small>
</li>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=60060863">ИМИТАЦИОННОЕ МОДЕЛИРОВАНИЕ: НЕКОТОРЫЕ АСПЕКТЫ ПРИМЕНЕНИЯ В ДИНАМИЧЕСКИХ ИНТЕЛЛЕКТУАЛЬНЫХ СИСТЕМАХ</a>
//
Инжиниринг предприятий и управление знаниями (ИП&amp;amp;УЗ-2023), 2023г.
<span class='text-muted'>

</span>
Стр. 303-310
</li>
<li><span class='label label-primary'>
журнал ВАК
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=54009174">Автоматизированное формирование персонифицированных стратегий обучения на основеобучающих интегрированных экспертных систем</a>
//
Приборы и системы. Управление, контроль, диагностика, 2023г.
<span class='text-muted'>
Вып. 6
</span>
Стр. 14-23
<small>
<a target="_blank" class="text-nowrap" href="http://doi.org/10.25791/pribor.6.2023.1413">doi
<i class="fa fa-share"></i>
</a></small>
</li>
<li><span class='label label-primary'>
Статья
</span>
<div class='label label-mint'>Web of Science &amp; Scopus</div>
<b class="p-l-5 p-r-5 ">Количество цитирований Scopus: 2</b>
<a target="_blank" href="https://www.doi.org/10.1134/S1054661823030409">Modern Architectures of Intelligent Tutoring Systems Based on Integrated Expert Systems: Features of the Approach to the Automated Formation of the Ontological Space of Knowledge and Skills of Students</a>
//
Pattern Recognition and Image Analysis, 2023
<span class='text-muted'>
Vol. 33, No. 3, Q3
</span>
pp. 491-497
<small>
<a target="_blank" class="text-nowrap" href="http://doi.org/10.1134/S1054661823030409">doi
<i class="fa fa-share"></i>
</a></small>
</li>
<li><span class='label label-primary'>
Статья
</span>
<div class='label label-mint'>Web of Science &amp; Scopus</div>
<b class="p-l-5 p-r-5 ">Количество цитирований Scopus: 2</b>
<a target="_blank" href="https://www.doi.org/10.1109/Inforino53888.2022.9782941">Automated Formation of the Unified Ontological Space of Students&#39; Knowledge and Skills to Implement Intellectual Tutoring Tasks Based on Tutoring Integrated Expert Systems</a>
//
2022 6th International Conference on Information Technologies in Engineering Education, Inforino 2022 - Proceedings, 2022
<span class='text-muted'>
TOP10
</span>

<small>
<a target="_blank" class="text-nowrap" href="http://doi.org/10.1109/Inforino53888.2022.9782941">doi
<i class="fa fa-share"></i>
</a></small>
</li>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=50346278">СОВРЕМЕННЫЕ АРХИТЕКТУРЫ ИНТЕЛЛЕКТУАЛЬНЫХ ОБУЧАЮЩИХ СИСТЕМ НА ОСНОВЕ ИНТЕГРИРОВАННЫХ ЭКСПЕРТНЫХ СИСТЕМ: ОСОБЕННОСТИ ПОДХОДА К АВТОМАТИЗИРОВАННОМУ ФОРМИРОВАНИЮ ОНТОЛОГИЧЕСКОГО ПРОСТРАНСТВА ЗНАНИЙ И УМЕНИЙ ОБУЧАЕМЫХ</a>
//
Двадцатая Национальная конференция по искусственному интеллекту с международным участием, КИИ-2022, 2022г.
<span class='text-muted'>

</span>
Стр. 218-231
</li>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=48717474">ОСОБЕННОСТИ ПОСТРОЕНИЯ ПРИКЛАДНОЙ ОНТОЛОГИИ ТИПОВЫХ АРХИТЕКТУР ИНТЕГРИРОВАННЫХ ЭКСПЕРТНЫХ СИСТЕМ С ИСПОЛЬЗОВАНИЕМ СРЕДСТВ ИНТЕЛЛЕКТУАЛЬНОЙ ПРОГРАММНОЙ СРЕДЫ КОМПЛЕКСА АТ-ТЕХНОЛОГИЯ</a>
//
Интегрированные модели и мягкие вычисления в искусственном интеллекте ИММВ-2022, 2022г.
<span class='text-muted'>

</span>
Стр. 188-196
</li>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=48695085">Онтологии как средство управления процессами построения и использования интегрированных экспертных систем различной архитектурной типологии</a>
//
Гибридные и синергетические интеллектуальные системы, 2022г.
<span class='text-muted'>

</span>
Стр. 190-198
<small>
<a target="_blank" class="text-nowrap" href="http://doi.org/10.5922/978-5-9971-0687-4-11">doi
<i class="fa fa-share"></i>
</a></small>
</li>
<li><span class='label label-primary'>
труды конференции РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=54193285">ОПЫТ РЕАЛИЗАЦИИ ОНТОЛОГИЧЕСКОГО ПОДХОДА ДЛЯ ПОСТРОЕНИЯ ИНТЕГРИРОВАННЫХ ЭКСПЕРТНЫХ СИСТЕМ РАЗЛИЧНОЙ АРХИТЕКТУРНОЙ ТИПОЛОГИИ</a>
//
Инжиниринг предприятий и управление знаниями (ИП&amp;amp;УЗ-2021), 2022г.
<span class='text-muted'>

</span>
Стр. 62-74
</li>
<li><span class='label label-primary'>
журнал РИНЦ
</span>

<a target="_blank" href="https://elibrary.ru/item.asp?id=46337348">ОСОБЕННОСТИ РЕАЛИЗАЦИИ ПРОТОТИПА ИНТЕГРИРОВАННОЙ ЭКСПЕРТНОЙ СИСТЕМЫ ДЛЯ КОМПЛЕКСНОЙ ДИАГНОСТИКИ ЗАБОЛЕВАНИЙ МОЛОЧНОЙ ЖЕЛЕЗЫ: ИНТЕГРАЦИЯ С ОБРАБОТКОЙ ИЗОБРАЖЕНИЙ</a>
//
Интегрированные модели и мягкие вычисления в искусственном интеллекте (ИММВ-2021), 2021г.
<span class='text-muted'>

</span>
Стр. 284-294
</li>
<li><span class='label label-primary'>
Статья
</span>
<div class='label label-mint'>Web of Science &amp; Scopus</div>
<b class="p-l-5 p-r-5 text-danger">Количество цитирований Scopus: 0</b>
<a target="_blank" href="https://www.scopus.com/record/display.uri?eid=2-s2.0-85116673572&amp;origin=resultslist">Features of implementation of prototype integrated expert system for comprehensive diagnosis of breast diseases: Integration with image processing</a>
//
CEUR Workshop Proceedings, 2021
<span class='text-muted'>
Vol. 2965, Q4
</span>
pp. 324-330
</li>
</ol>
</div>
</div>
<div class='panel panel-default'>
<div class='panel-heading' id='user_conferences' role='tab'>
<h4 class='panel-title'>
<a data-toggle="collapse" data-parent="#articles_panel" role="button" aria-expanded="true" aria-controls="user_conferences_collapse" href="#user_conferences_collapse">Участие в конференциях
</a></h4>
</div>
<div class='panel-collapse collapse panel-body' id='user_conferences_collapse' role='tabpanel'>
<p class='text-muted'>Показаны конференции за последние 3 года</p>
<div class='panel panel-info'>
<div class='panel-body'>Информация о конференциях не найдена</div>
</div>
</div>
</div>
</div>
</div>

<div class='user-posts'>


</div>


</div>
</div>
<p class="text-muted">Согласие на обработку персональных данных получено в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных»</p>

<footer>
<div class='pull-left'>
<div><span>© НИЯУ МИФИ, 2015–2024</span></div>
</div>
<div class='pull-right'>Разработано в УИМООП НИЯУ МИФИ</div>
<div class='clearfix'></div>
</footer>

</div>
</div>
</div>
<div id='modal_wrapper'></div>
</body>
</html>
'''

print(hmp.parse_Teacher(q))