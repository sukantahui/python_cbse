import pymysql
import datetime


def createDatabase():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS books")

    # Create table as per requirement
    sql = """CREATE TABLE books (
              id bigint unsigned NOT NULL AUTO_INCREMENT,
              serial varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              book_name varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              author varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              genre varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              publisher varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
              publication int unsigned DEFAULT NULL,
              member_id bigint unsigned DEFAULT NULL,
              issue_date datetime DEFAULT NULL,
              is_issued tinyint DEFAULT '0',
              PRIMARY KEY (id)
            ) ENGINE=InnoDB"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS members")

    sql = """CREATE TABLE members (
           id BIGINT UNSIGNED AUTO_INCREMENT,
           serial varchar(20) DEFAULT NULL,
           member_name VARCHAR(255),
           phone VARCHAR(20),
           doj DATETIME,
           display TINYINT DEFAULT '1',
           inforce TINYINT DEFAULT '1',
          PRIMARY KEY (id)
        ) ENGINE = InnoDB"""
    cursor.execute(sql)
    # adding self as a member
    now = datetime.datetime.utcnow()
    addMember(1, "self", "9143656893", now)
    addBook('1001', 'Fundamentals of Wavelets', 'Goswami, Jaideva', 'tech', 'Wiley', 2128, 1)
    addBook('1002', 'Data Smart', 'Foreman, John', 'tech', 'Wiley', 2135, 1)
    addBook('1003', 'God Created the Integers', 'Hawking, Stephen', 'tech', 'Penguin', 2097, 1)
    addBook('1004', 'Superfreakonomics', 'Dubner, Stephen', 'science', 'HarperCollins', 2079, 1)
    addBook('1005', 'Orientalism', 'Said, Edward', 'nonfiction', 'Penguin', 2097, 1)
    addBook('1006', 'Nature of Statistical Learning Theory, The', 'Vapnik, Vladimir', 'tech', 'Springer', 2130, 1)
    addBook('1007', 'Integration of the Indian States', 'Menon, V P', 'nonfiction', 'Orient Blackswan', 2117, 1)
    addBook('1008', 'Drunkards Walk, The', 'Mlodinow, Leonard', 'science', 'Penguin', 2097, 1)
    addBook('1009', 'Image Processing & Mathematical Morphology', 'Shih, Frank', 'tech', 'CRC', 2141, 1)
    addBook('1010', 'How to Think Like Sherlock Holmes', 'Konnikova, Maria', 'nonfiction', 'Penguin', 2140, 1)

    addBook('1011', 'Data Scientists at Work', 'Sebastian Gutierrez', 'tech', 'Apress', 2130, 1)
    addBook('1012', 'Slaughterhouse Five', 'Vonnegut, Kurt', 'fiction', 'Random House', 2098, 1)
    addBook('1013', 'Birth of a Theorem', 'Villani, Cedric', 'science', 'Bodley Head', 2134, 1)
    addBook('1014', 'Structure & Interpretation of Computer Programs', 'Sussman, Gerald', 'tech', 'MIT Press', 2140, 1)
    addBook('1015', 'Age of Wrath, The', 'Eraly, Abraham', 'nonfiction', 'Penguin', 2138, 1)
    addBook('1016', 'Trial, The', 'Kafka, Frank', 'fiction', 'Random House', 2098, 1)
    addBook('1017', 'Statistical Decision Theory', 'Pratt, John', 'tech', 'MIT Press', 2136, 1)
    addBook('1018', 'Data Mining Handbook', 'Nisbet, Robert', 'tech', 'Apress', 2142, 1)
    addBook('1019', 'New Machiavelli, The', 'Wells, H. G.', 'fiction', 'Penguin', 2080, 1)
    addBook('1020', 'Physics & Philosophy', 'Heisenberg, Werner', 'philosophy', 'Penguin', 2097, 1)

    addBook('1021','Making Software','Oram, Andy','tech','OReilly',2132,1)
    addBook('1022','Analysis, Vol I','Tao, Terence','tech','HBA',2148,1)
    addBook('1023','Machine Learning for Hackers','Conway, Drew','tech','OReilly',2133,1)
    addBook('1024','Signal and the Noise, The','Silver, Nate','tech','Penguin',2133,1)
    addBook('1025','Python for Data Analysis','McKinney, Wes','tech','OReilly',2133,1)
    addBook('1026','Introduction to Algorithms','Cormen, Thomas','tech','MIT Press',2134,1)
    addBook('1027','Beautiful and the Damned, The','Deb, Siddhartha','nonfiction','Penguin',2098,1)
    addBook('1028','Outsider, The','Camus, Albert','fiction','Penguin',2098,1)
    addBook('1029','Complete Sherlock Holmes, The - Vol I','Doyle, Arthur Conan','fiction','Random House',2076,1)
    addBook('1030','Complete Sherlock Holmes, The - Vol II','Doyle, Arthur Conan','fiction','Random House',2076,1)
    addBook('1031','Wealth of Nations, The','Smith, Adam','science','Random House',2075,1)
    addBook('1032','Pillars of the Earth, The','Follett, Ken','fiction','Random House',2076,1)
    addBook('1033','Mein Kampf','Hitler, Adolf','nonfiction','Rupa',2112,1)
    addBook('1034','Tao of Physics, The','Capra, Fritjof','science','Penguin',2079,1)
    addBook('1035','Surely Youre Joking Mr Feynman','Feynman, Richard','science','Random House',2098,1)
    addBook('1036','Farewell to Arms, A','Hemingway, Ernest','fiction','Rupa',2079,1)
    addBook('1037','Veteran, The','Forsyth, Frederick','fiction','Transworld',2077,1)
    addBook('1038','False Impressions','Archer, Jeffery','fiction','Pan',2077,1)
    addBook('1039','Last Lecture, The','Pausch, Randy','nonfiction','Hyperion',2097,1)
    addBook('1040','Return of the Primitive','Rand, Ayn','philosophy','Penguin',2102,1)

    addBook('1041', 'Jurassic Park', 'Crichton, Michael', 'fiction', 'Random House', 2074, 1)
    addBook('1042', 'Russian Journal, A', 'Steinbeck, John', 'nonfiction', 'Penguin', 2096, 1)
    addBook('1043', 'Tales of Mystery and Imagination', 'Poe, Edgar Allen', 'fiction', 'HarperCollins', 2072, 1)
    addBook('1044', 'Freakonomics', 'Dubner, Stephen', 'science', 'Penguin', 2097, 1)
    addBook('1045', 'Hidden Connections, The', 'Capra, Fritjof', 'science', 'HarperCollins', 2097, 1)
    addBook('1046', 'Story of Philosophy, The', 'Durant, Will', 'philosophy', 'Pocket', 2070, 1)
    addBook('1047', 'Asami Asami', 'Deshpande, P L', 'fiction', 'Mauj', 2105, 1)
    addBook('1048', 'Journal of a Novel', 'Steinbeck, John', 'fiction', 'Penguin', 2096, 1)
    addBook('1049', 'Once There Was a War', 'Steinbeck, John', 'nonfiction', 'Penguin', 2096, 1)
    addBook('1050', 'Moon is Down, The', 'Steinbeck, John', 'fiction', 'Penguin', 2096, 1)
    addBook('1051', 'Brethren, The', 'Grisham, John', 'fiction', 'Random House', 2074, 1)
    addBook('1052', 'In a Free State', 'Naipaul, V. S.', 'fiction', 'Rupa', 2096, 1)
    addBook('1053', 'Catch 22', 'Heller, Joseph', 'fiction', 'Random House', 2078, 1)
    addBook('1054', 'Complete Mastermind, The', 'BBC', 'nonfiction', 'BBC', 2078, 1)
    addBook('1055', 'Dylan on Dylan', 'Dylan, Bob', 'nonfiction', 'Random House', 2097, 1)
    addBook('1056', 'Soft Computing & Intelligent Systems', 'Gupta, Madan', 'tech', 'Elsevier', 2142, 1)
    addBook('1057', 'Textbook of Economic Theory', 'Stonier, Alfred', 'tech', 'Pearson', 2142, 1)
    addBook('1058', 'Econometric Analysis', 'Greene, W. H.', 'tech', 'Pearson', 2142, 1)
    addBook('1059', 'Learning OpenCV', 'Bradsky, Gary', 'tech', 'O Reilly',2132,1)
    addBook('1060', 'Data Structures Using C & C++', 'Tanenbaum, Andrew', 'tech', 'Prentice Hall', 2135, 1)
    addBook('1061', 'Computer Vision, A Modern Approach', 'Forsyth, David', 'tech', 'Pearson', 2155, 1)
    addBook('1062', 'Principles of Communication Systems', 'Taub, Schilling', 'tech', 'TMH', 2140, 1)
    addBook('1063', 'Let Us C', 'Kanetkar, Yashwant', 'tech', 'Prentice Hall', 2113, 1)
    addBook('1064', 'Amulet of Samarkand, The', 'Stroud, Jonathan', 'fiction', 'Random House', 2079, 1)
    addBook('1065', 'Crime and Punishment', 'Dostoevsky, Fyodor', 'fiction', 'Penguin', 2080, 1)
    addBook('1066', 'Angels & Demons', 'Brown, Dan', 'fiction', 'Random House', 2078, 1)
    addBook('1067', 'Argumentative Indian, The', 'Sen, Amartya', 'nonfiction', 'Picador', 2109, 1)
    addBook('1068', 'Sea of Poppies', 'Ghosh, Amitav', 'fiction', 'Penguin', 2097, 1)
    addBook('1069', 'Idea of Justice, The', 'Sen, Amartya', 'philosophy', 'Penguin', 2112, 1)
    addBook('1070', 'Raisin in the Sun, A', 'Hansberry, Lorraine', 'fiction', 'Penguin', 2075, 1)
    addBook('1071', 'All the Presidents  Men','Woodward, Bob','nonfiction','Random House',2077,1)
    addBook('1072', 'Prisoner of Birth, A', 'Archer, Jeffery', 'fiction', 'Pan', 2076, 1)
    addBook('1073', 'Scoop!', 'Nayar, Kuldip', 'nonfiction', 'HarperCollins', 2116, 1)
    addBook('1074', 'Ahe Manohar Tari', 'Deshpande, Sunita', 'nonfiction', 'Mauj', 2113, 1)
    addBook('1075', 'Last Mughal, The', 'Dalrymple, William', 'nonfiction', 'Penguin', 2099, 1)
    addBook('1076', 'Social Choice & Welfare, Vol 39 No. 1', 'Various', 'tech', 'Springer', 2135, 1)
    addBook('1077', 'Radiowaril Bhashane & Shrutika', 'Deshpande, P L', 'nonfiction', 'Mauj', 2113, 1)
    addBook('1078', 'Gun Gayin Awadi', 'Deshpande, P L', 'nonfiction', 'Mauj', 2112, 1)
    addBook('1079', 'Aghal Paghal', 'Deshpande, P L', 'nonfiction', 'Mauj', 2112, 1)
    addBook('1080', 'Maqta-e-Ghalib', 'Garg, Sanjay', 'nonfiction', 'Mauj', 2121, 1)
    addBook('1081', 'Beyond Degrees', 'Garg, Sanjay', 'philosophy', 'HarperCollins', 2122, 1)
    addBook('1082', 'Manasa', 'Kale, V P', 'nonfiction', 'Mauj', 2113, 1)
    addBook('1083', 'India from Midnight to Milennium', 'Tharoor, Shashi', 'nonfiction', 'Penguin', 2098, 1)
    addBook('1084', 'Worlds Greatest Trials, The','Tharoor, Shashi','nonfiction','',2110,1)
    addBook('1085', 'Great Indian Novel, The', 'Tharoor, Shashi', 'fiction', 'Penguin', 2098, 1)
    addBook('1086', 'O Jerusalem!', 'Lapierre, Dominique', 'nonfiction', 'vikas', 2117, 1)
    addBook('1087', 'City of Joy, The', 'Lapierre, Dominique', 'fiction', 'vikas', 2077, 1)
    addBook('1088', 'Freedom at Midnight', 'Lapierre, Dominique', 'nonfiction', 'vikas', 2067, 1)
    addBook('1089', 'Winter of Our Discontent, The', 'Steinbeck, John', 'fiction', 'Penguin', 2096, 1)
    addBook('1090', 'On Education', 'Russell, Bertrand', 'philosophy', 'Routledge', 2103, 1)
    addBook('1091', 'Free Will', 'Harris, Sam', 'nonfiction', 'FreePress', 2103, 1)
    addBook('1092', 'Bookless in Baghdad', 'Tharoor, Shashi', 'nonfiction', 'Penguin', 2106, 1)
    addBook('1093', 'Case of the Lame Canary, The', 'Gardner, Earle Stanley', 'fiction', 'Penguin', 2079, 1)
    addBook('1094', 'Theory of Everything, The', 'Hawking, Stephen', 'science', 'Jaico', 2117, 1)
    addBook('1095', 'New Markets & Other Essays', 'Drucker, Peter', 'science', 'Penguin', 2076, 1)
    addBook('1096', 'Electric Universe', 'Bodanis, David', 'science', 'Penguin', 2101, 1)
    addBook('1097', 'Hunchback of Notre Dame, The', 'Hugo, Victor', 'fiction', 'Random House', 2075, 1)
    addBook('1098', 'Burning Bright', 'Steinbeck, John', 'fiction', 'Penguin', 2075, 1)
    addBook('1099', 'Age of Discontuinity, The', 'Drucker, Peter', 'nonfiction', 'Random House', 2078, 1)
    addBook('1100', 'Doctor in the Nude', 'Gordon, Richard', 'fiction', 'Penguin', 2079, 1)
    addBook('1101', 'Down and Out in Paris & London', 'Orwell, George', 'nonfiction', 'Penguin', 2079, 1)
    addBook('1102', 'Identity & Violence', 'Sen, Amartya', 'philosophy', 'Penguin', 2119, 1)
    addBook('1103', 'Beyond the Three Seas', 'Dalrymple, William', 'nonfiction', 'Random House', 2097, 1)
    addBook('1104', 'Worlds Greatest Short Stories, The','Dalrymple, William','fiction','Jaico',2117,1)
    addBook('1105', 'Talking Straight', 'Iacoca, Lee', 'nonfiction', 'Jaico', 2075, 1)
    addBook('1106', 'Maughams Collected    Short    Stories, Vol    3','Maugham, WilliamS',' fiction','Vintage',2071,1)
    addBook('1107', 'Phantom of Manhattan, The', 'Forsyth, Frederick', 'fiction', 'Vintage', 2080, 1)
    addBook('1108', 'Ashenden of The British Agent', 'Maugham, William S', 'fiction', 'Vintage', 2060, 1)
    addBook('1109', 'Zen & The Art of Motorcycle Maintenance', 'Pirsig, Robert', 'philosophy', 'Vintage', 2072, 1)
    addBook('1110', 'Great War for Civilization, The', 'Fisk, Robert', 'nonfiction', 'HarperCollins', 2097, 1)
    addBook('1111', 'We the Living', 'Rand, Ayn', 'fiction', 'Penguin', 2078, 1)
    addBook('1112', 'Artist and the Mathematician, The', 'Aczel, Amir', 'science', 'HighStakes', 2086, 1)
    addBook('1113', 'History of Western Philosophy', 'Russell, Bertrand', 'philosophy', 'Routledge', 2113, 1)
    addBook('1114', 'Selected Short Stories', 'Russell, Bertrand', 'fiction', 'Jaico', 2115, 1)
    addBook('1115', 'Rationality & Freedom', 'Sen, Amartya', 'science', 'Springer', 2113, 1)
    addBook('1116', 'Clash of Civilizations and Remaking of the World Order', 'Huntington, Samuel', 'nonfiction','Simon&Schuster', 2128, 1)
    addBook('1117', 'Uncommon Wisdom', 'Capra, Fritjof', 'nonfiction', 'Fontana', 2097, 1)
    addBook('1118', 'One', 'Bach, Richard', 'nonfiction', 'Dell', 2072, 1)
    addBook('1119', 'Karl Marx Biography', 'Bach, Richard', 'nonfiction', 'Dell', 2062, 1)
    addBook('1120', 'To Sir With Love', 'Braithwaite', 'fiction', 'Penguin', 2097, 1)
    addBook('1121', 'Half A Life', 'Naipaul, V S', 'fiction', 'Penguin', 2096, 1)
    addBook('1122', 'Discovery of India, The', 'Nehru, Jawaharlal', 'nonfiction', 'Penguin', 2130, 1)
    addBook('1123', 'Apulki', 'Deshpande, P L', 'nonfiction', 'Penguin', 2111, 1)
    addBook('1124', 'Unpopular Essays', 'Russell, Bertrand', 'philosophy', 'Penguin', 2098, 1)
    addBook('1125', 'Deceiver, The', 'Forsyth, Frederick', 'fiction', 'Penguin', 2078, 1)
    addBook('1126', 'Veil: Secret Wars of the CIA', 'Woodward, Bob', 'nonfiction', 'Penguin', 2071, 1)
    addBook('1127', 'Char Shabda', 'Deshpande, P L', 'nonfiction', 'Penguin', 2114, 1)
    addBook('1128', 'Rosy is My Relative', 'Durrell, Gerald', 'fiction', 'Penguin', 2076, 1)
    addBook('1129', 'Moon and Sixpence, The', 'Maugham, William S', 'fiction', 'Penguin', 2080, 1)
    addBook('1130', 'Political Philosophers', 'Maugham, William S', 'philosophy', 'Penguin', 2062, 1)
    addBook('1131', 'Short History of the World, A', 'Wells, H G', 'nonfiction', 'Penguin', 2097, 1)
    addBook('1132', 'Trembling of a Leaf, The', 'Maugham, William S', 'fiction', 'Penguin', 2105, 1)
    addBook('1133', 'Doctor on the Brain', 'Gordon, Richard', 'fiction', 'Penguin', 2104, 1)
    addBook('1134', 'Simpsons & Their Mathematical Secrets', 'Singh, Simon', 'science', 'Penguin', 2133, 1)
    addBook('1135', 'Pattern Classification', 'Duda, Hart', 'tech', 'Penguin', 2141, 1)
    addBook('1136', 'From Beirut to Jerusalem', 'Friedman, Thomas', 'nonfiction', 'Penguin', 2102, 1)
    addBook('1137', 'Code Book, The', 'Singh, Simon', 'science', 'Penguin', 2097, 1)
    addBook('1138', 'Age of the Warrior, The', 'Fisk, Robert', 'nonfiction', 'Penguin', 2097, 1)
    addBook('1139', 'Final Crisis', 'Fisk, Robert', 'fiction', 'Penguin', 2157, 1)
    addBook('1140', 'Killing Joke, The', 'Fisk, Robert', 'fiction', 'Penguin', 2183, 1)
    addBook('1141', 'Flashpoint', 'Fisk, Robert', 'fiction', 'Penguin', 2165, 1)
    addBook('1142', 'Batman Earth One', 'Fisk, Robert', 'fiction', 'Penguin', 2165, 1)
    addBook('1143', 'Crisis on Infinite Earths', 'Fisk, Robert', 'fiction', 'Penguin', 2158, 1)
    addBook('1144', 'Numbers Behind Numb3rs, The', 'Devlin, Keith', 'science', 'Penguin', 2102, 1)
    addBook('1145', 'Superman Earth One - 1', 'Devlin, Keith', 'fiction', 'Penguin', 2159, 1)
    addBook('1146', 'Superman Earth One - 2', 'Devlin, Keith', 'fiction', 'Penguin', 2158, 1)
    addBook('1147', 'Justice League: Throne of Atlantis', 'Devlin, Keith', 'fiction', 'Penguin', 2158, 1)
    addBook('1148', 'Justice League: The Villains Journey',' Devlin, Keith ','  fiction',' Penguin',2158,1)
    addBook('1149', 'Death of Superman, The', 'Devlin, Keith', 'fiction', 'Penguin', 2158, 1)
    addBook('1150', 'History of the DC Universe', 'Devlin, Keith', 'fiction', 'Penguin', 2158, 1)
    addBook('1151', 'Batman: The Long Halloween', 'Devlin, Keith', 'fiction', 'Penguin', 2158, 1)
    addBook('1152', 'Life in Letters, A', 'Steinbeck, John', 'nonfiction', 'Penguin', 2096, 1)
    addBook('1153', 'Information, The', 'Gleick, James', 'science', 'Penguin', 2133, 1)
    addBook('1154', 'Journal of Economics, vol 106 No 3', 'Gleick, James', 'science', 'Penguin', 2135, 1)
    addBook('1155', 'Elements of Information Theory', 'Thomas, Joy', 'tech', 'Penguin', 2129, 1)
    addBook('1156', 'Power Electronics - Rashid', 'Rashid, Muhammad', 'tech', 'Penguin', 2135, 1)
    addBook('1157', 'Power Electronics - Mohan', 'Mohan, Ned', 'tech', 'Penguin', 2137, 1)
    addBook('1158', 'Neural Networks', 'Haykin, Simon', 'tech', 'Penguin', 2140, 1)
    addBook('1159', 'Grapes of Wrath, The', 'Steinbeck, John', 'fiction', 'Penguin', 2096, 1)
    addBook('1160', 'Vyakti ani Valli', 'Deshpande, P L', 'nonfiction', 'Penguin', 2111, 1)
    addBook('1161', 'Statistical Learning Theory', 'Vapnik, Vladimir', 'tech', 'Penguin', 2128, 1)
    addBook('1162', 'Empire of the Mughal - The Tainted Throne', 'Rutherford, Alex', 'nonfiction', 'Penguin', 2080, 1)
    addBook('1163', 'Empire of the Mughal - Brothers at War', 'Rutherford, Alex', 'nonfiction', 'Penguin', 2080, 1)
    addBook('1164', 'Empire of the Mughal - Ruler of the World', 'Rutherford, Alex', 'nonfiction', 'Penguin', 2080, 1)
    addBook('1165', 'Empire of the Mughal - The Serpents Tooth','Rutherford, Alex','nonfiction',' Penguin ',2080,1)
    addBook('1166', 'Empire of the Mughal - Raiders from the North', 'Rutherford, Alex', 'nonfiction', 'Penguin', 2080,1)
    addBook('1167', 'Mossad', 'Baz-Zohar, Michael', 'nonfiction', 'Penguin', 2136, 1)
    addBook('1168', 'Jim Corbett Omnibus', 'Corbett, Jim', 'nonfiction', 'Penguin', 2123, 1)
    addBook('1169', '20000 Leagues Under the Sea', 'Verne, Jules', 'fiction', 'Penguin', 2090, 1)
    addBook('1170', 'Batatyachi Chal', 'Deshpande P L', 'fiction', 'Penguin', 2100, 1)
    addBook('1171', 'Hafasavnuk', 'Deshpande P L', 'fiction', 'Penguin', 2111, 1)
    addBook('1172', 'Urlasurla', 'Deshpande P L', 'fiction', 'Penguin', 2111, 1)
    addBook('1173', 'Pointers in C', 'Kanetkar, Yashwant', 'tech', 'Penguin', 2113, 1)
    addBook('1174', 'Cathedral and the Bazaar, The', 'Raymond, Eric', 'tech', 'Penguin', 2117, 1)
    addBook('1175', 'Design with OpAmps', 'Franco, Sergio', 'tech', 'Penguin', 2140, 1)
    addBook('1176', 'Think Complexity', 'Downey, Allen', 'tech', 'Penguin', 2130, 1)
    addBook('1177', 'Devils Advocate, The ','  West, Morris  ','  fiction  ','  Penguin   ',2078,1)
    addBook('1178', 'Ayn Rand Answers', 'Rand, Ayn', 'philosophy', 'Penguin', 2103, 1)
    addBook('1179', 'Philosophy: Who Needs It', 'Rand, Ayn', 'philosophy', 'Penguin', 2071, 1)
    addBook('1180', 'World    s Great Thinkers, The ',' Rand, Ayn ','  science   ','   Penguin    ',2089,1)
    addBook('1181', 'Data Analysis with Open Source Tools', 'Janert, Phillip', 'tech', 'Penguin', 2130, 1)
    addBook('1182', 'Broca    s  Brain  ','  Sagan, Carl  ','  science  ','  Penguin  ',2074,1)
    addBook('1183', 'Men of Mathematics', 'Bell, E T', 'science', 'Penguin', 2117, 1)
    addBook('1184', 'Oxford book of Modern Science Writing', 'Dawkins, Richard', 'science', 'Penguin', 2140, 1)
    addBook('1185', 'Justice, Judiciary and Democracy', 'Ranjan, Sudhanshu', 'nonfiction', 'Penguin', 2124, 1)
    addBook('1186', 'Arthashastra, The', 'Kautiyla', 'philosophy', 'Penguin', 2114, 1)
    addBook('1187', 'We the People', 'Palkhivala', 'philosophy', 'Penguin', 2116, 1)
    addBook('1188', 'We the Nation', 'Palkhivala', 'philosophy', 'Penguin', 2116, 1)
    addBook('1189', 'Courtroom Genius, The', 'Sorabjee', 'nonfiction', 'Penguin', 2117, 1)
    addBook('1190', 'Dongri to Dubai', 'Zaidi, Hussain', 'nonfiction', 'Penguin', 2116, 1)
    addBook('1191', 'History of England, Foundation', 'Ackroyd, Peter', 'nonfiction', 'Penguin', 2097, 1)
    addBook('1192', 'City of Djinns', 'Dalrymple, William', 'nonfiction', 'Penguin', 2098, 1)
    addBook('1193', 'India    s    Legal    System    ','    Nariman    ','    nonfiction    ','    Penguin    ',2077,1)
    addBook('1194', 'More Tears to Cry', 'Sassoon, Jean', 'fiction', 'Penguin', 2135, 1)
    addBook('1195', 'Ropemaker, The', 'Dickinson, Peter', 'fiction', 'Penguin', 2096, 1)
    addBook('1196', 'Angels & Demons', 'Brown, Dan', 'fiction', 'Penguin', 2070, 1)
    addBook('1197', 'Judge, The', 'Brown, Dan', 'fiction', 'Penguin', 2070, 1)
    addBook('1198', 'Attorney, The', 'Brown, Dan', 'fiction', 'Penguin', 2070, 1)
    addBook('1199', 'Prince, The', 'Machiavelli', 'fiction', 'Penguin', 2073, 1)
    addBook('1200', 'Eyeless in Gaza', 'Huxley, Aldous', 'fiction', 'Penguin', 2080, 1)
    addBook('1201', 'Tales of Beedle the Bard', 'Rowling, J K', 'fiction', 'Penguin', 2084, 1)
    addBook('1202', 'Girl with the Dragon Tattoo', 'Larsson, Steig', 'fiction', 'Penguin', 2079, 1)
    addBook('1203', 'Girl who kicked the Hornet   s    Nest    ','    Larsson, Steig    ','    fiction    ','   Penguin    ',2079,1)
    addBook('1204', 'Girl who played with Fire', 'Larsson, Steig', 'fiction', 'Penguin', 2079, 1)
    addBook('1205', 'Batman Handbook', 'Larsson, Steig', 'fiction', 'Penguin', 2170, 1)
    addBook('1206', 'Murphy    s    Law    ','    Larsson, Steig    ','    philosophy    ','    Penguin    ',2078,1)
    addBook('1207', 'Structure and Randomness', 'Tao, Terence', 'science', 'Penguin', 2152, 1)
    addBook('1208', 'Image Processing with MATLAB', 'Eddins, Steve', 'tech', 'Penguin', 2141, 1)
    addBook('1209', 'Animal Farm', 'Orwell, George', 'fiction', 'Penguin', 2080, 1)
    addBook('1210', 'Idiot, The', 'Dostoevsky, Fyodor', 'fiction', 'Penguin', 2097, 1)
    addBook('1211', 'Christmas Carol, A', 'Dickens, Charles', 'fiction', 'Penguin', 2096, 1)

    # createDatabase()


# adding book
def addBook(serial, name, in_author, in_genre, publisher, publication, member_id):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """insert into books (
                                   id
                                  ,serial
                                  ,book_name
                                  ,author
                                  ,genre
                                  ,publisher
                                  ,publication
                                  ,member_id
                                ) VALUES (
                                  NULL, %s,%s, %s, %s,%s,%s,%s
                                )"""
    try:
        # Execute the SQL command
        cursor.execute(sql, (serial, name, in_author, in_genre, publisher, publication, member_id))
        # Commit your changes in the database
        print("done")
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def showBooks():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM books"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            book_id = row[0]
            serial = row[1]
            book_name = row[2]
            author = row[3]
            publisher = row[4]
            publication = row[5]
            # Now print fetched result
            print("ID = %s,Serial = %s,Title = %s,Author = %s,Publisher = %s, Edition = %s" % (
                book_id, serial, book_name, author, publisher, publication))
    except:
        print("Error: unable to fetch data")
    # disconnect from server
    db.close()


def getBookIdBySerial(find_serial):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM books where serial = %s"
    try:
        # Execute the SQL command
        cursor.execute(sql, find_serial)
        # Fetch all the rows in a list of lists.
        row = cursor.fetchone()
        if row == None:
            return 0
        else:
            return row[0]

    except:
        return 0
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def getBookBySerial(find_serial):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM books where serial = %s"
    try:
        # Execute the SQL command
        cursor.execute(sql, find_serial)
        # Fetch all the rows in a list of lists.
        row = cursor.fetchone()
        return row

    except:
        return 0
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def updateBooks(update_book_id, name, author, publisher, publication):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "update books SET  book_name = %s ,author = %s,publisher = %s ,publication = %s  WHERE id = %s"

    try:
        # Execute the SQL command
        cursor.execute(sql, (name, author, publisher, publication, update_book_id))
        print('updated')
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print('unable to update')
        db.rollback()

    # disconnect from server
    db.close()


def deleteBooks(book_id):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM books WHERE id = '%d'" % (book_id)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        print("Book Deleted", book_id)
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


# adding member functions
def addMember(in_serial, in_name, in_phone, in_date):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """insert into members (
           id
          ,serial
          ,member_name
          ,phone
          ,doj
        ) VALUES (NULL,%s,%s,%s,%s
        )"""
    try:
        # Execute the SQL command
        cursor.execute(sql, (in_serial, in_name, in_phone, in_date))
        # Commit your changes in the database
        print("Member added")
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def getMemberBySerial(in_serial):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM members where serial = %s"
    try:
        # Execute the SQL command
        cursor.execute(sql, in_serial)
        # Fetch all the rows in a list of lists.
        row = cursor.fetchone()
        if row is None:
            pass
        else:
            return row

    except:
        return 0
        print("Error: unable to fetch data")

    # disconnect from server
    db.close()


def updateMember(in_id, in_name, in_phone):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "update members SET  member_name = %s ,phone = %s WHERE id = %s "

    try:
        # Execute the SQL command
        cursor.execute(sql, (in_name, in_phone, in_id))
        print('Member updated')
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print('unable to update')
        db.rollback()

    # disconnect from server
    db.close()


def deleteMember(member_id):
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "delete from members where id = %s"
    try:
        # Execute the SQL command
        cursor.execute(sql, (member_id))
        # Commit your changes in the database
        print("\t\t\t\tMember Deleted")
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def showMembers():
    # Open database connection
    db = pymysql.connect(host='localhost', database='library_db', user='root', password='sukantahui')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "select * from members where inforce=1 and display=1"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            member_id = row[0]
            temp_serial = row[1]
            temp_name = row[2]
            temp_phone = row[3]
            temp_doj = row[4]
            # Now print fetched result
            print("ID = %s,Serial = %s,Name = %s,Phone = %s,DOJ = %s" % (
                member_id, temp_serial, temp_name, temp_phone, temp_doj))
    except:
        print("Error: unable to fetch data")
    # disconnect from server
    db.close()


# addBook("1234", "Suman Ghosh", "Dinesh", "ABP", 2020)
# showBooks()

today = datetime.date.today()
# createDatabase()
# addBook("1234", "xSuman Ghosh", "Dinesh", "ABP", 2020)
# showBooks()
# updateBooks()
# deleteBooks(7)


project = "SBJW"
print("Welcome to ", project)
while True:
    print("Main Menu")
    print("1. book")
    print("2. Member")
    print("3. Transaction")
    print("4. Report")
    print("8. Refresh Database")
    print("9. Exit")

    ch1 = int(input("Enter your Choice in Main Menu: "))
    if ch1 == 8:
        createDatabase()
        print("Database is created successfully")
        continue
    if ch1 == 9:
        break
    elif ch1 < 1 or ch1 > 5:
        print("Wrong choice ...............")

    if ch1 == 1:
        # Book area
        while True:
            print("\tBook Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t9. Exit Book Menu")
            chBook = int(input("\tEnter your Choice in Book Menu: "))
            if chBook == 9:
                break
            elif chBook < 1 or chBook > 5:
                print("\tWrong choice in book menu ...............")

            if chBook == 1:
                serial = input("\t\tEnter book Serial: ")
                title = input("\t\tBook Title: ")
                author = input("\t\tAuthor Name: ")
                genre = input("\t\tGenre: ")
                publisher = input("\t\tPublisher: ")
                edition = int(input("\t\tEdition: "))
                addBook(serial, title, author, genre, publisher, edition, 1)
            if chBook == 2:
                # showBooks()
                book_serial = input("\t\tEnter Book serial to search: ")
                book_id = getBookIdBySerial(book_serial)
                if book_id == 0:
                    print("This serial does not exist")
                else:
                    title = input("\t\tBook Title: ")
                    author = input("\t\tAuthor Name: ")
                    publisher = input("\t\tPublisher: ")
                    edition = int(input("\t\tEdition: "))
                    updateBooks(book_id, title, author, publisher, edition)
            if chBook == 3:
                book_serial = input("\t\tEnter Book serial to search for delete: ")
                book_id = getBookIdBySerial(book_serial)
                if book_id == 0:
                    print("This serial does not exist")
                else:
                    deleteBooks(book_id)
            if chBook == 4:
                showBooks()
    if ch1 == 2:
        while True:
            print("\tMember Menu")
            print("\t1. Add")
            print("\t2. Update")
            print("\t3. Delete")
            print("\t4. Display")
            print("\t9. Exit Member Menu")
            chMember = int(input("\tEnter your Choice in Member Menu: "))
            if chMember == 9:
                break
            elif chMember < 1 or chMember > 5:
                print("\tWrong choice in member menu ...............")

            if chMember == 1:
                serial = input("\t\tEnter Member Serial: ")
                name = input("\t\tMember Name: ")
                phone = input("\t\tPhone: ")
                now = datetime.datetime.utcnow()
                addMember(serial, name, phone, now)

            if chMember == 2:
                serial = input("Enter member serial to edit")
                member = getMemberBySerial(serial)
                print('You want to  update {0} and its contact is {1}'.format(member[2], member[3]))
                name = input("New name for member")
                phone = input("New phone for member")
                updateMember(member[0], name, phone)
            if chMember == 3:
                serial = input("Enter member serial to delete")
                member = getMemberBySerial(serial)
                print('You want to  delete {0} and its contact is {1}'.format(member[2], member[3]))
                deleteMember(member[0])

            if chMember == 4:
                print("Members are: ")
                showMembers()
    if ch1 == 3:
        while True:
            print("\tTransaction Menu")
            print("\t1. Assign book to Member")
            print("\t2. Return book from Member")
            print("\t9. Exit Book Menu")
            chTransaction = int(input("Enter your Choice for Transaction: "))
            if chTransaction == 9:
                break
            elif ch1 < 1 or ch1 > 2:
                print("Wrong choice ...............")
            if chTransaction == 1:
                temp_book_serial = input("Enter book Serial: ")
                book = getBookBySerial(temp_book_serial)
                print('Book Title is {}, written by {} and published by {} edition year is {}'.format(book[2], book[3],
                                                                                                      book[4], book[5]))
                if book[6] == 1:
                    print("This book is available in Library")
                    temp_member_serial = input("Enter member serial: ")
                    member = getMemberBySerial(temp_book_serial)
                    print(member)
                    print('Please wait assigning book {0} to member {1}'.format(book[2], member[2]))
                else:
                    print("This book is not available")
