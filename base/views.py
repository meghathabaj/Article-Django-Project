from django.shortcuts import render

article_data = [
    {
        'id': 1,
        'image': 'https://thumbs.dreamstime.com/b/beautiful-rain-forest-ang-ka-nature-trail-doi-inthanon-national-park-thailand-36703721.jpg',
        'title': 'All about nature',
        'desc': 'Nature is a beautiful gift that surrounds us with greenery, fresh air, colorful flowers, and peaceful landscapes. From green forests to flowing rivers and beautiful mountains, nature brings a sense of calm and happiness. Spending time in nature helps us relax, refresh our minds, and appreciate the beauty of the world around us.'},
    {
        'id': 2,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfloMvUTyWpJ8y2DgJsvf1zsviqbGrC8e-tQ58rs7uMGBLcWwujO4yPAo&s=10',
        'title': 'All about cat',
        'desc': 'Cats are beautiful, playful, and intelligent animals known for their soft fur, bright eyes, and charming personalities. They enjoy exploring their surroundings, playing with toys, and spending peaceful moments with their owners. Their cute and loving nature makes them wonderful companions.'},
    {
        'id': 3,
        'image': 'https://img.magnific.com/free-photo/smiling-young-woman-holding-retro-camera_329181-142.jpg?semt=ais_hybrid&w=740&q=80',
        'title': 'All About Beautyy',
        'desc' :  'Beatiful gilr with beautiful eyes',
    }
]

news_data = [
    {
        'id':4,
        'image': 'https://images.news18.com/ibnlive/uploads/2025/08/World-News-AI-Blog-2025-07-71d087050940689d8621058405992e8c.jpg',
        'desc':  '“Stay informed with fresh news and updates across different categories.”',
    },
    {
        'id':5,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ55isUodQUeUx5Vp225wIXGWhtF5bFXx-UxZzDnyAFukjDPpmpuSKkXloT&s=10',
        'desc':  'Get the latest news, trending stories, and important updates from around the world.”',
    },
    {
        'id': 5,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdmmzoBSotifhQ7DDGS_smDZVSNE2qeH1Dvkrb8_04T5SiDQdKnhflEqQ&s=10',
        'desc':  '“Latest news and updates covering technology, sports, business, entertainment, and more.”',
    },
    {
        'id': 6,
        'image': 'https://i.ytimg.com/vi/GotlA1KKWoo/sddefault.jpg?v=6a90ae34',
        'desc':  'Your source for the latest updates, breaking news, and trending topics.”',
    },
    {
        'id': 7,
        'image': 'https://img.etimg.com/thumb/width-420,height-315,imgsize-145474,resizemode-75,msid-134716333/news/economy/finance/single-window-gst-registration-for-multistate-businesses-set-for-pilot-this-week.jpg',
        'desc':  'Bringing you the latest headlines, stories, and updates every day.”' ,

    },
    {
        'id': 8,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUiN7_JhWWl6n89C7kG3m5UPdAHUVoEfEmy6eUfpSMBGnSKK4AZSSIFfKR&s=10',
        'desc':  'Catch up on what’s happening around the world with the latest news.”',
    },


]
blogs_data = [
    {
        'id': 9,
        'image': 'https://media.architecturaldigest.com/photos/67acb9b0339bcbaaadeb91b5/1:1/w_4000,h_4000,c_limit/GettyImages-873536102.jpg',
        'desc':  '“The Taj Mahal stands as a timeless symbol of love, admired for its breathtaking beauty, magnificent architecture, and rich history.”',
    },
    {
        'id': 10,
        'image': 'https://www.avis.co.in/blog/wp-content/uploads/2018/08/paris-600x375.jpg',
        'desc':  '“The Eiffel Tower is one of France’s most iconic landmarks, known for its stunning architecture and breathtaking views of Paris. It stands as a timeless symbol of beauty, romance, and the spirit of France.”',

    },
    {
        'id': 11,
        'image': 'https://blog.lemontreehotels.com/wp-content/uploads/2025/02/Places-to-Visit-in-Delhi.jpg',
        'desc':  '“India Gate is a magnificent war memorial in the heart of New Delhi, honoring the brave Indian soldiers who sacrificed their lives for the country. Its grand architecture and historic significance make it one of India’s most iconic landmarks.”',

    },
    {
        'id': 12,
        'image': 'https://www.mysoretourism.org.in/images/v2/headers/places-to-visit-near-mysore-header-bangalore-tourism.jpg.jpg',
        'desc':  '“Mysore Palace is a magnificent royal landmark in Karnataka, famous for its grand architecture, beautiful interiors, and rich history. Its stunning illumination and royal charm make it one of India’s most beautiful palaces.”',

    },
    {
        'id': 13,
        'image': 'https://media.assettype.com/outlooktraveller/2024-08-08/3t0dz8am/shutterstock_1845146593.jpg',
        'desc':  '“Historical places are the treasures of our past, preserving stories, cultures, and traditions for future generations. They remind us of the people, events, and civilizations that shaped our world.”',
    },
    {
        'id': 14,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOCOT1fd6S8Q8tw9JrvXC-cpom9puArQv88zFVTUyIFeT6Orf7aNyEMGMv&s=10',
        'desc':  'Gol Gumbaz is a magnificent historical monument in Vijayapura, Karnataka, famous for its massive dome and remarkable architecture. Built in the 17th century, it is one of the most iconic landmarks of Karnataka and a symbol of India’s rich architectural heritage.”',
    }
]
sports_data = [
    {
        'id': 15,
        'image': 'https://media.istockphoto.com/id/2291845504/photo/badminton-sport-equipments-racket-and-shuttlecock-on-indoor-floor-of-badminton-court-concept.jpg?s=612x612&w=0&k=20&c=KFU5fnMuwvDR-v_S5-RE4B2i7WSnOtRWJT_WjcaDG3k=',
        'desc':  '“Table tennis is a fast and exciting indoor sport played between two or four players. It requires quick reflexes, focus, and good coordination, making it a fun and energetic game for people of all ages.”',
    },
    {
        'id': 16,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI1TIjVTO_ngg830HGU9b_5DrAve2INPSSXr0G46TgTd8RcwU4oW4OcM0&s=10',
        'desc':  '“Basketball is a fast-paced and exciting team sport played between two teams. It requires teamwork, speed, skill, and quick decision-making, making it one of the most popular sports around the world.”',
    },
    {
        'id': 17,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSupDoYECZIqF7SI14dan0TqYoTMccXg1omjZ8MmqpODSz5MWe0gnPlW2oy&s=10',
        'desc':  '“Cricket is a popular and exciting sport played between two teams. It combines skill, strategy, teamwork, and patience, making it one of the most loved sports, especially in countries like India.”',
    },
    {
        'id': 18,
        'image': 'https://c.ndtvimg.com/2025-01/ifk7svq4_kho-kho-match-ani_160x120_17_January_25.jpg',
        'desc':  '“Kho-Kho is a traditional Indian team sport that combines speed, agility, and teamwork. It is an exciting game that requires quick thinking, sharp reflexes, and excellent coordination.”',
    },
    {
        'id': 19,
        'image': 'https://www.aichi-nagoya2026.org/wp-content/uploads/2025/10/Kabaddi%E2%92%B8OCA.png',
        'desc':  'Kabaddi is a traditional Indian team sport that combines strength, speed, strategy, and teamwork. It is an exciting game that tests a player’s stamina, agility, and quick decision-making.',
    },
    {
        'id': 20,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRE0UV42Ay0a3gp2mY_HowjqGHdFpJaVUzGvaCFjI_feiJKoeNjb8uRlzdn&s=10',
        'desc':  '“Table tennis is a quick and enjoyable indoor sport that requires speed, concentration, and fast reflexes. Played with paddles and a small ball, it is a fun and competitive game enjoyed around the world.”',
    },
]
international_data = [
    {
        'id': 21,
        'image': 'https://yehaindia.com/wp-content/uploads/2020/02/Chess-1-1024x678.jpg',
        'desc':  '“Chess is a timeless game of strategy and intelligence played between two players. It challenges the mind, improves concentration and critical thinking, and is enjoyed by millions of people around the world.”',
    },
    {
        'id': 22,
        'image': 'https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_sm_2x/f_auto/primary/appdnx7p8kng3vw1j17e',
        'desc':  '“Hockey is a fast-paced and exciting team sport that requires skill, speed, teamwork, and quick decision-making. Played with a stick and ball or puck, it is enjoyed by millions of people around the world.”',
    },
    {
        'id': 23,
        'image': 'https://images.indianexpress.com/2020/03/carrom_incopy.jpg',
        'desc':  'Carrom is a popular indoor board game that combines skill, accuracy, and concentration. Players use a striker to pocket the carrom pieces into the corner pockets, making it an enjoyable and competitive game for people of all ages.',

    },
    {
        'id': 24,
        'image': 'https://gamingbolt.com/wp-content/uploads/2010/08/international-athletics-start-line.jpg',
        'desc':  'Athletics is a collection of competitive sports that includes running, jumping, and throwing events. It requires speed, strength, endurance, and skill, making it one of the most popular and fundamental forms of sport around the world.',
    },
    {
        'id': 25,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYHOOTljrChGmfLGYOfEGIWCyPoYG_TItl87FXH1zhjg&s',
        'desc':  'Basketball is a fast-paced and exciting team sport played between two teams. It requires teamwork, speed, skill, and quick decision-making, making it one of the most popular sports around the world.',
    },
    {
        'id': 26,
        'image': 'https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5302x3535+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F2e%2Fe8%2F5328221c483d9e37e3314f247d64%2Fap26175465618124.jpg',
        'desc':  'The Olympics is a major international sporting event where athletes from around the world compete in various sports. It celebrates talent, dedication, teamwork, and sportsmanship while bringing nations together through the spirit of competition.',

    },

]


def home(request):
    context = {'data':article_data}
    return render(request,'home.html',context)

def news(request):
    context = {'data':news_data}
    return render(request,'news.html',context)

def sports(request):
    context = {'data':sports_data}
    return render(request,'sports.html',context)

def international(request):
    context = {'data':international_data}
    return render(request,'international.html',context)

def blogs(request):
    context = {'data':blogs_data}
    return render(request,'blogs.html',context)

def about(request):
    return render(request,'about.html')

def read(request, id):
    all_data = article_data + news_data + blogs_data + sports_data + international_data

    for i in all_data:
        if i['id'] == id:
            context = {'data': i}
            return render(request, 'read.html', context)


















































































































1