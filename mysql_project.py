import mysql.connector 

mydb = mysql.connector.connect(host ="127.0.0.1", user = "root", password = "Newyork1624!", database = "Project")
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Project")

mycursor.execute("SHOW DATABASES")

mycursor.execute("CREATE TABLE Songs (song_id VARCHAR(255), song_name VARCHAR(255), artist_name VARCHAR(255), album_name VARCHAR(255), release_date INT(255), genre VARCHAR(255), duration INT(255))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO Songs (song_id, song_name, artist_name, album_name, release_date, genre, duration) VALUES (%s, %s, %s, %s, %s, %s, %s)"
songs = [('S001', 'Anti-Hero', 'Taylor Swift', 'Midnights', 2022, 'Pop', 200),
('S002', 'Efecto', 'Bad Bunny', 'Un Verano Sin Ti', 2022, 'Reggaeton', 180),
('S003', 'Dynamite', 'BTS', 'BE', 2020, 'K-Pop', 199),
('S004', 'Happier Than Ever', 'Billie Eilish', 'Happier Than Ever', 2021, 'Alternative', 298),
('S005', 'Levitating', 'Dua Lipa', 'Future Nostalgia', 2020, 'Pop', 203),
('S006', 'God''s Plan', 'Drake', 'Scorpion', 2018, 'Hip-Hop', 198),
('S007', 'DESPECHÁ', 'Rosalía', 'MOTOMAMI', 2022, 'Flamenco Pop', 165),
('S008', 'Shape of You', 'Ed Sheeran', '÷ (Divide)', 2017, 'Pop', 233),
('S009', 'Blinding Lights', 'The Weeknd', 'After Hours', 2020, 'Synthpop', 200),
('S010', 'PROVENZA', 'Karol G', 'MAÑANA SERÁ BONITO', 2023, 'Reggaeton', 175),
('S011', 'Kill Bill', 'SZA', 'SOS', 2022, 'R&B', 153),
('S012', 'Calm Down', 'Rema', 'Rave & Roses', 2022, 'Afrobeats', 180),
('S013', 'Boy''s a Liar Pt. 2', 'Ice Spice', 'Like..?', 2023, 'Rap', 145),
('S014', 'As It Was', 'Harry Styles', 'Harry''s House', 2022, 'Pop Rock', 167),
('S015', 'vampire', 'Olivia Rodrigo', 'GUTS', 2023, 'Indie Pop', 215),
('S016', 'Amarillo', 'J Balvin', 'Colores', 2020, 'Reggaeton', 172),
('S017', 'Woman', 'Doja Cat', 'Planet Her', 2021, 'Pop', 170),
('S018', 'Chantaje', 'Shakira', 'El Dorado', 2016, 'Latin Pop', 180),
('S019', 'Case 143', 'Stray Kids', 'MAXIDENT', 2022, 'K-Pop', 190),
('S020', 'Shut Down', 'BLACKPINK', 'BORN PINK', 2022, 'K-Pop', 183),
('S021', 'Seven', 'Jung Kook', 'GOLDEN', 2023, 'K-Pop', 187),
('S022', 'Doin'' Time', 'Lana Del Rey', 'Norman F***ing Rockwell!', 2019, 'Indie Pop', 197),
('S023', 'HUMBLE.', 'Kendrick Lamar', 'DAMN.', 2017, 'Hip-Hop', 177),
('S024', 'Her', 'Megan Thee Stallion', 'Traumazine', 2022, 'Rap', 164),
('S025', 'SICKO MODE', 'Travis Scott', 'ASTROWORLD', 2018, 'Hip-Hop', 312),
('S026', 'Ella Baila Sola', 'Peso Pluma', 'GÉNESIS', 2023, 'Regional Mexican', 174),
('S027', 'MAMIII', 'Becky G', 'MALA SANTA', 2022, 'Reggaeton', 170),
('S028', 'Rinse & Repeat', 'Riton', 'Destiny', 2016, 'House', 218),
('S029', 'Nonbinary', 'Arca', 'Kick I', 2020, 'Experimental', 193),
('S030', 'Envolver', 'Anitta', 'Versions of Me', 2022, 'Funk Carioca', 180),
('S031', 'Delilah (pull me out of this)', 'Fred again..', 'Actual Life 3', 2022, 'Electronic', 210),
('S032', 'Eat Your Young', 'Hozier', 'Unreal Unearth', 2023, 'Indie Rock', 235),
('S033', 'Found', 'Tems', 'If Orange Was a Place', 2021, 'Afrobeats', 188),
('S034', 'Nonsense', 'Sabrina Carpenter', 'emails i can’t send', 2022, 'Pop', 160),
('S035', 'Green Light', 'Lorde', 'Melodrama', 2017, 'Art Pop', 231),
('S036', 'Santé', 'Stromae', 'Multitude', 2022, 'Chanson Pop', 194),
('S037', 'Delete Forever', 'Grimes', 'Miss Anthropocene', 2020, 'Synthpop', 182),
('S038', 'Darkest Hour', 'Sevdaliza', 'ISON', 2017, 'Trip Hop', 242),
('S039', 'Loving Is Easy', 'Rex Orange County', 'Apricot Princess', 2017, 'Indie Pop', 161),
('S040', 'Dance Monkey', 'Tones and I', 'The Kids Are Coming', 2019, 'Alternative', 209),
('S041', 'Take My Breath', 'The Weeknd', 'Dawn FM', 2022, 'Synthpop', 220),
('S042', '10%', 'KAYTRA', 'BUBBA', 2019, 'Electronic', 190),
('S043', 'Je te vois enfin', 'Christine and the Queens', 'People I’ve Been Sad', 2020, 'Electropop', 195),
('S044', 'Feet Don''t Fail Me Now', 'Joy Crookes', 'Not Your Muse', 2021, 'Soul', 175),
('S045', 'Caroline', 'Amine', 'Limbo', 2020, 'Hip-Hop', 220),
('S046', 'telepatía', 'Kali Uchis', 'Sin Miedo', 2020, 'Dream Pop', 165),
('S047', 'Simmer', 'Mahalia', 'Love and Compromise', 2019, 'R&B', 194),
('S048', 'Paper Planes', 'M.I.A.', 'Kala', 2007, 'Worldbeat', 203),
('S049', 'Unholy', 'Sam Smith', 'Gloria', 2023, 'Pop', 157),
('S050', 'Bags', 'Clairo', 'Immunity', 2019, 'Indie Rock', 234),
('S051', 'Heather', 'Conan Gray', 'Superache', 2022, 'Indie Pop', 210),
('S052', 'From the Start', 'Laufey', 'Bewitched', 2023, 'Jazz Pop', 189),
('S053', 'Water', 'Tyla', 'Water', 2023, 'Afropop', 180),
('S054', 'It Was a Good Day', 'Ice Cube', 'The Predator', 1992, 'Hip-Hop', 273),
('S055', 'Three Heads*', 'Jean Dawson', 'CHAOS NOW*', 2022, 'Experimental Rap', 206),
('S056', 'soso', 'Omah Lay', 'Boy Alone', 2022, 'Afrobeats', 204),
('S057', 'Tonight', 'Phoenix', 'Alpha Zulu', 2022, 'Indie Rock', 191),
('S058', 'Nobody', 'Mitski', 'Laurel Hell', 2022, 'Indie Rock', 206),
('S059', 'High School in Jakarta', 'NIKI', 'Nicole', 2022, 'Indie Pop', 202),
('S060', 'Snail', 'BENEE', 'Hey u x', 2020, 'Alt Pop', 175)]

mycursor.executemany(sqlFormula, songs)

mydb.commit()

mycursor.execute("CREATE TABLE Artists (song_id VARCHAR(255), artist_name VARCHAR(255), city VARCHAR(255), country VARCHAR(255), followers VARCHAR(255), gender VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO Artists (song_id, artist_name, city, country, followers, gender) VALUES (%s, %s, %s, %s, %s, %s)"

artists = [('A001', 'Taylor Swift', 'Reading', 'USA', '92,000,000', 'Female'),
('A002', 'Bad Bunny', 'San Juan', 'Puerto Rico', '72,000,000', 'Male'),
('A003', 'BTS', 'Seoul', 'South Korea', '75,000,000', 'Male'),
('A004', 'Billie Eilish', 'Los Angeles', 'USA', '68,000,000', 'Female'),
('A005', 'Dua Lipa', 'London', 'UK', '58,000,000', 'Female'),
('A006', 'Drake', 'Toronto', 'Canada', '85,000,000', 'Male'),
('A007', 'Rosalía', 'Barcelona', 'Spain', '33,000,000', 'Female'),
('A008', 'Ed Sheeran', 'Halifax', 'UK', '79,000,000', 'Male'),
('A009', 'The Weeknd', 'Toronto', 'Canada', '90,000,000', 'Male'),
('A010', 'Karol G', 'Medellín', 'Colombia', '42,000,000', 'Female'),
('A011', 'SZA', 'St. Louis', 'USA', '39,000,000', 'Female'),
('A012', 'Rema', 'Benin City', 'Nigeria', '25,000,000', 'Male'),
('A013', 'Ice Spice', 'New York City', 'USA', '20,000,000', 'Female'),
('A014', 'Harry Styles', 'Redditch', 'UK', '64,000,000', 'Male'),
('A015', 'Olivia Rodrigo', 'Temecula', 'USA', '50,000,000', 'Female'),
('A016', 'J Balvin', 'Medellín', 'Colombia', '45,000,000', 'Male'),
('A017', 'Doja Cat', 'Los Angeles', 'USA', '55,000,000', 'Female'),
('A018', 'Shakira', 'Barranquilla', 'Colombia', '48,000,000', 'Female'),
('A019', 'Stray Kids', 'Seoul', 'South Korea', '40,000,000', 'Male'),
('A020', 'BLACKPINK', 'Seoul', 'South Korea', '70,000,000', 'Female'),
('A021', 'Jung Kook', 'Busan', 'South Korea', '36,000,000', 'Male'),
('A022', 'Lana Del Rey', 'Lake Placid', 'USA', '30,000,000', 'Female'),
('A023', 'Kendrick Lamar', 'Compton', 'USA', '43,000,000', 'Male'),
('A024', 'Megan Thee Stallion', 'Houston', 'USA', '28,000,000', 'Female'),
('A025', 'Travis Scott', 'Houston', 'USA', '44,000,000', 'Male'),
('A026', 'Peso Pluma', 'Zapopan', 'Mexico', '22,000,000', 'Male'),
('A027', 'Becky G', 'Inglewood', 'USA', '18,000,000', 'Female'),
('A028', 'Riton', 'Newcastle', 'UK', '5,000,000', 'Male'),
('A029', 'Arca', 'Caracas', 'Venezuela', '8,000,000', 'Nonbinary'),
('A030', 'Anitta', 'Rio de Janeiro', 'Brazil', '32,000,000', 'Female'),
('A031', 'Fred again..', 'London', 'UK', '15,000,000', 'Male'),
('A032', 'Hozier', 'Bray', 'Ireland', '27,000,000', 'Male'),
('A033', 'Tems', 'Lagos', 'Nigeria', '14,000,000', 'Female'),
('A034', 'Sabrina Carpenter', 'Lehigh Valley', 'USA', '19,000,000', 'Female'),
('A035', 'Lorde', 'Auckland', 'New Zealand', '25,000,000', 'Female'),
('A036', 'Stromae', 'Brussels', 'Belgium', '12,000,000', 'Male'),
('A037', 'Grimes', 'Vancouver', 'Canada', '10,000,000', 'Female'),
('A038', 'Sevdaliza', 'Rotterdam', 'Netherlands', '7,000,000', 'Female'),
('A039', 'Rex Orange County', 'Haslemere', 'UK', '9,000,000', 'Male'),
('A040', 'Tones and I', 'Melbourne', 'Australia', '13,000,000', 'Female'),
('A041', 'RIT', 'Oakland', 'USA', '1,200,000', 'Female'),
('A042', 'KAYTRA', 'Montreal', 'Canada', '2,800,000', 'Male'),
('A043', 'Libianca', 'Minneapolis', 'USA', '3,100,000', 'Female'),
('A044', 'Joy Crookes', 'London', 'UK', '6,000,000', 'Female'),
('A045', 'Amine', 'Portland', 'USA', '7,500,000', 'Male'),
('A046', 'Kali Uchis', 'Alexandria', 'USA', '11,000,000', 'Female'),
('A047', 'Mahalia', 'Leicester', 'UK', '5,500,000', 'Female'),
('A048', 'M.I.A.', 'London', 'UK', '9,500,000', 'Female'),
('A049', 'Sam Smith', 'London', 'UK', '35,000,000', 'Nonbinary'),
('A050', 'Clairo', 'Carlisle', 'USA', '6,800,000', 'Female'),
('A051', 'Conan Gray', 'Lemon Grove', 'USA', '12,000,000', 'Male'),
('A052', 'Laufey', 'Reykjavík', 'Iceland', '4,200,000', 'Female'),
('A053', 'Tyla', 'Johannesburg', 'South Africa', '3,800,000', 'Female'),
('A054', 'Ice Cube', 'Los Angeles', 'USA', '5,000,000', 'Male'),
('A055', 'Jean Dawson', 'San Diego', 'USA', '2,300,000', 'Male'),
('A056', 'Omah Lay', 'Port Harcourt', 'Nigeria', '6,000,000', 'Male'),
('A057', 'Phoenix', 'Versailles', 'France', '4,900,000', 'Male'),
('A058', 'Mitski', 'New York City', 'USA', '7,100,000', 'Female'),
('A059', 'NIKI', 'Jakarta', 'Indonesia', '8,400,000', 'Female'),
('A060', 'BENEE', 'Auckland', 'New Zealand', '5,900,000', 'Female')]

mycursor.executemany(sqlFormula, artists)

mydb.commit()


mycursor.execute("CREATE TABLE Playlists (playlist_id VARCHAR(255), playlist_name VARCHAR(255), songs VARCHAR(255), genre VARCHAR(255), listens INT(255))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO Playlists (playlist_name, playlist_id, genre, songs, listens) VALUES (%s, %s, %s, %s, %s)"

playlists = [('Chill Vibes', 'U001', 'Reggaeton', 'S022,S049,S010,S030,S035', 4284),
('Workout Mix', 'U016', 'Hip-Hop', 'S043,S002,S047,S057,S004,S058,S035,S010,S017,S027,S028', 3444),
('Party Starters', 'U006', 'Lo-Fi', 'S006,S033,S020,S004,S041', 8591),
('Study Time', 'U005', 'K-Pop', 'S023,S048,S008,S038,S034,S041,S004,S060,S002,S015', 6217),
('Throwback Hits', 'U017', 'Hip-Hop', 'S017,S036,S049,S051,S039,S029,S013,S048,S047', 8559),
('Indie Essentials', 'U004', 'Hip-Hop', 'S002,S026,S053,S054,S027,S006,S057', 7116),
('Late Night Drive', 'U005', 'Hip-Hop', 'S044,S053,S059,S042,S048,S051,S018,S015,S046,S006', 4996),
('Top 2020s', 'U014', 'Hip-Hop', 'S058,S002,S015,S054,S049,S060,S004,S030,S022,S011,S047', 5453),
('Summer Feels', 'U006', 'Reggaeton', 'S001,S035,S007,S040,S010,S021', 8566),
('Global Grooves', 'U013', 'Country', 'S015,S039,S020,S007,S048,S044,S010,S050,S057,S004,S002,S031', 3865),
('K-Pop Anthems', 'U002', 'K-Pop', 'S029,S016,S043,S035,S059,S015', 2432),
('Latin Fire', 'U003', 'Indie', 'S033,S052,S007,S030,S056,S054,S046,S021,S037', 5081),
('Mood Boosters', 'U003', 'Latin', 'S046,S057,S016,S010,S039,S024', 912),
('Lo-Fi Lounge', 'U008', 'Latin', 'S028,S016,S004,S051,S048,S057,S007,S056,S038,S006,S022,S042', 6640),
('R&B Favorites', 'U006', 'Afrobeats', 'S058,S057,S036,S030,S020,S027,S044,S054,S011,S012,S008,S045', 3841),
('Pop Parade', 'U004', 'Hip-Hop', 'S058,S034,S013,S053,S043,S010,S009,S044,S045,S014,S008', 4562),
('Rap Rotation', 'U010', 'Latin', 'S013,S053,S052,S024,S054,S016', 1509),
('Electronic Edge', 'U012', 'Synthpop', 'S004,S025,S006,S042,S038,S016,S045,S036,S019,S029', 9488),
('Country Roads', 'U007', 'Afrobeats', 'S032,S015,S037,S030,S055,S027,S025,S008,S039', 6379),
('Alt Rock Rewind', 'U008', 'Country', 'S023,S045,S032,S005,S044,S052,S007,S015,S041,S010', 2901),
('Sunday Morning', 'U020', 'Synthpop', 'S011,S010,S037,S012,S048,S005,S026,S018,S059,S022,S047,S009', 4187),
('Feel Good Hits', 'U001', 'Rock', 'S031,S030,S033,S051,S041', 1540),
('Melancholy Moods', 'U005', 'K-Pop', 'S056,S060,S010,S025,S035,S003,S040,S006,S027', 4047),
('Golden Hour', 'U015', 'K-Pop', 'S026,S029,S005,S009,S031,S053,S025,S022,S012', 9190),
('New Music Friday', 'U005', 'Alternative', 'S041,S038,S004,S020,S034,S003,S048,S045,S029,S012,S013', 3911),
('Sad Girl Autumn', 'U008', 'Indie', 'S011,S008,S040,S031,S043,S010,S032,S019,S005,S006', 9422),
('Viral Tracks', 'U006', 'Indie', 'S012,S054,S055,S027,S042,S032,S010,S033', 6021),
('Lush Landscapes', 'U005', 'Afrobeats', 'S012,S043,S050,S007,S044,S010,S018,S036,S046,S049,S016', 6577),
('Night Shift', 'U011', 'Hip-Hop', 'S055,S057,S050,S004,S031,S012,S053,S013,S033,S059', 5067),
('Daily Mix Pop', 'U004', 'Afrobeats', 'S035,S009,S039,S051,S031,S020,S006,S007', 7428),
('Road Trip', 'U008', 'Jazz', 'S059,S044,S007,S002,S032,S013,S021,S042,S033,S045,S048,S020', 5023),
('Bedroom Pop', 'U018', 'R&B', 'S005,S044,S028,S004,S032,S001,S056,S025,S014,S020,S036', 4734),
('Post-Party Cooldown', 'U010', 'K-Pop', 'S010,S019,S006,S052,S047', 8613),
('Coffeehouse Chill', 'U014', 'Alternative', 'S023,S029,S002,S049,S054', 4974),
('Heavy Rotation', 'U006', 'Afrobeats', 'S034,S028,S021,S014,S022', 2624),
('Soothing Sounds', 'U014', 'Electronic', 'S041,S024,S033,S035,S026,S058,S009,S030,S051', 3551),
('City Lights', 'U003', 'Synthpop', 'S030,S040,S058,S028,S027,S038,S023,S055,S017', 1209),
('Indie Folk Mix', 'U003', 'Lo-Fi', 'S032,S039,S041,S049,S029,S034', 1314),
('Dancefloor Heat', 'U001', 'R&B', 'S060,S026,S014,S042,S056,S023,S039,S054,S038,S020,S028,S016', 7034),
('Indie Rock Revival', 'U011', 'Alternative', 'S002,S030,S009,S019,S035,S032,S027,S004,S016,S008,S045,S014', 205),
('Festival Season', 'U003', 'Afrobeats', 'S049,S016,S019,S004,S045,S021', 6839),
('Hits of the Decade', 'U010', 'K-Pop', 'S043,S050,S019,S042,S052,S011,S008,S003,S025,S060,S032', 8063),
('Nostalgia Trip', 'U003', 'Indie', 'S040,S042,S043,S049,S006,S008,S048,S003,S056', 4014),
('Top Picks', 'U015', 'Hip-Hop', 'S009,S048,S056,S010,S016,S035,S005,S055,S047,S011', 1763),
('Power Hour', 'U014', 'Latin', 'S045,S028,S037,S048,S053,S006,S056', 3893),
('Fresh Finds', 'U013', 'Country', 'S053,S055,S013,S046,S003', 5121),
('Breakup Ballads', 'U015', 'Pop', 'S003,S015,S022,S017,S055', 4264),
('Feel the Beat', 'U019', 'Alternative', 'S054,S008,S056,S057,S013,S032,S055,S016,S014,S059,S023', 8966),
('Tranquil Tones', 'U005', 'Indie', 'S037,S039,S005,S059,S057,S027,S058,S040,S056,S018,S042', 1316),
('Hype Mode', 'U012', 'Reggaeton', 'S024,S032,S047,S038,S037', 9135),
('Sonic Bloom', 'U013', 'Indie', 'S035,S055,S021,S019,S013,S027,S025,S042,S011,S045,S048,S031', 5374),
('Soulful Sundays', 'U010', 'Afrobeats', 'S051,S011,S005,S012,S038,S036,S048,S037,S004', 6922),
('Midnight Moves', 'U019', 'Lo-Fi', 'S049,S009,S016,S011,S014', 3614),
('Gen Z Gems', 'U008', 'Jazz', 'S029,S004,S030,S039,S059,S042,S022,S008,S049,S060,S025', 281),
('Alt Nation', 'U011', 'Hip-Hop', 'S004,S045,S009,S051,S011,S047,S025,S056,S043,S003', 8815),
('Late Night Loops', 'U004', 'Lo-Fi', 'S017,S015,S047,S009,S042,S016,S034,S021', 5814),
('Downtempo Dreams', 'U016', 'Jazz', 'S059,S041,S044,S018,S009,S013,S005,S031,S058,S032', 8427),
('Champagne Problems', 'U004', 'Alternative', 'S017,S002,S018,S005,S060,S051,S026,S052,S054', 4553),
('Femme Fatale', 'U013', 'Alternative', 'S059,S036,S031,S055,S004,S010,S026,S017,S025,S060', 7835)]

mycursor.executemany(sqlFormula, playlists)

mydb.commit()


mycursor.execute("CREATE TABLE Albums (album_id VARCHAR(255), album_name VARCHAR(255), artist_name VARCHAR(255), artist_id VARCHAR(255), release_date INT(255), genre VARCHAR(255), tracks INT(255), revenue FLOAT(3))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO Albums (album_id, album_name, artist_name, artist_id, release_date, genre, tracks, revenue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

albums = [('AL001', 'Midnights', 'Taylor Swift', 'A001', 2022, 'Pop', 13, 194),
('AL002', 'Un Verano Sin Ti', 'Bad Bunny', 'A002', 2022, 'Reggaeton', 23, 476),
('AL003', 'BE', 'BTS', 'A003', 2020, 'K-Pop', 8, 369),
('AL004', 'Happier Than Ever', 'Billie Eilish', 'A004', 2021, 'Pop', 16, 303),
('AL005', 'Future Nostalgia', 'Dua Lipa', 'A005', 2020, 'Pop', 11, 86),
('AL006', 'Certified Lover Boy', 'Drake', 'A006', 2021, 'Hip-Hop', 21, 86),
('AL007', 'Motomami', 'Rosalía', 'A007', 2022, 'Reggaeton', 16, 38),
('AL008', 'x', 'Ed Sheeran', 'A008', 2014, 'Pop', 16, 434),
('AL009', 'Dawn FM', 'The Weeknd', 'A009', 2022, 'R&B', 16, 305),
('AL010', 'Mañana Será Bonito', 'Karol G', 'A010', 2023, 'Reggaeton', 15, 357),
('AL011', 'SOS', 'SZA', 'A011', 2022, 'R&B', 23, 20),
('AL012', 'Rave & Roses', 'Rema', 'A012', 2022, 'Afrobeats', 16, 485),
('AL013', 'Like...?', 'Ice Spice', 'A013', 2023, 'Hip-Hop', 5, 418),
('AL014', 'Harry''s House', 'Harry Styles', 'A014', 2022, 'Pop Rock', 13, 114),
('AL015', 'Guts', 'Olivia Rodrigo', 'A015', 2023, 'Pop Rock', 12, 99),
('AL016', 'Jose', 'J Balvin', 'A016', 2021, 'Reggaeton', 18, 100),
('AL017', 'Planet Her', 'Doja Cat', 'A017', 2021, 'Pop', 14, 159),
('AL018', 'El Dorado', 'Shakira', 'A018', 2017, 'Pop', 13, 267),
('AL019', '5-Star', 'Stray Kids', 'A019', 2023, 'K-Pop', 10, 222),
('AL020', 'Born Pink', 'BLACKPINK', 'A020', 2022, 'K-Pop', 8, 153),
('AL021', 'Golden', 'Jung Kook', 'A021', 2023, 'Pop', 8, 310),
('AL022', 'Did You Know That There''s a Tunnel Under Ocean Blvd', 'Lana Del Rey', 'A022', 2023, 'Indie Pop', 16, 78),
('AL023', 'Mr. Morale & The Big Steppers', 'Kendrick Lamar', 'A023', 2022, 'Hip-Hop', 18, 153),
('AL024', 'Traumazine', 'Megan Thee Stallion', 'A024', 2022, 'Hip-Hop', 18, 190),
('AL025', 'Utopia', 'Travis Scott', 'A025', 2023, 'Hip-Hop', 19, 233),
('AL026', 'Génesis', 'Peso Pluma', 'A026', 2023, 'Regional Mexican', 16, 395),
('AL027', 'Esquinas', 'Becky G', 'A027', 2023, 'Latin Pop', 12, 108),
('AL028', 'Be The Illuminati', 'Riton', 'A028', 2019, 'Electronic', 10, 262),
('AL029', 'kick i', 'Arca', 'A029', 2020, 'Experimental', 18, 300),
('AL030', 'Versions of Me', 'Anitta', 'A030', 2022, 'Pop', 15, 33),
('AL031', 'Actual Life 3 (January 1–September 9 2022)', 'Fred again..', 'A031', 2023, 'Electronic', 17, 307.7),
('AL032', 'Unreal Unearth', 'Hozier', 'A032', 2023, 'Indie Rock', 15, 93.56),
('AL033', 'If Orange Was a Place', 'Tems', 'A033', 2021, 'Alternative R&B', 10, 41.88),
('AL034', 'Emails I Can''t Send', 'Sabrina Carpenter', 'A034', 2022, 'Pop', 13, 474.95),
('AL035', 'Solar Power', 'Lorde', 'A035', 2021, 'Indie Pop', 12, 483.16),
('AL036', 'Multitude', 'Stromae', 'A036', 2022, 'Electronic', 15, 406.11),
('AL037', 'Miss Anthropocene', 'Grimes', 'A037', 2020, 'Electronic', 13, 159.26),
('AL038', 'Shabrang', 'Sevdaliza', 'A038', 2020, 'Art Pop', 14, 57.86),
('AL039', 'Pony', 'Rex Orange County', 'A039', 2022, 'Indie Pop', 16, 345.27),
('AL040', 'Welcome to the Madhouse', 'Tones and I', 'A040', 2021, 'Pop', 12, 225.67),
('AL041', 'Unknown Album', 'RIT', 'A041', 2023, 'Unknown', 10, 69.8),
('AL042', 'Bubba', 'Kaytranada', 'A042', 2019, 'Electronic', 13, 252.64),
('AL043', 'Church Girl', 'Libianca', 'A043', 2023, 'Afropop', 7, 26.85),
('AL044', 'Skin', 'Joy Crookes', 'A044', 2022, 'Soul', 11, 455.57),
('AL045', 'Limbo', 'Aminé', 'A045', 2020, 'Hip-Hop', 18, 136.8),
('AL046', 'Isolation', 'Kali Uchis', 'A046', 2018, 'R&B/Soul', 13, 334.64),
('AL047', 'Love and Compromise', 'Mahalia', 'A047', 2019, 'R&B', 17, 162.74),
('AL048', 'AIM', 'M.I.A.', 'A048', 2016, 'Electronic/Hip-Hop', 12, 264.83),
('AL049', 'To Die For', 'Sam Smith', 'A049', 2020, 'Pop/Soul', 9, 277.89),
('AL050', 'Sling', 'Clairo', 'A050', 2021, 'Indie Pop', 11, 100.58),
('AL051', 'Superache', 'Conan Gray', 'A051', 2022, 'Pop', 16, 485.1),
('AL052', 'Everything I Know About Love', 'Laufey', 'A052', 2023, 'Jazz Pop', 11, 389.82),
('AL053', 'Debut EP', 'Tyla', 'A053', 2023, 'R&B', 6, 470.35),
('AL054', 'AmeriKKKa''s Most Wanted', 'Ice Cube', 'A054', 1990, 'Hip-Hop', 16, 448.47),
('AL055', 'Chaos Now', 'Jean Dawson', 'A055', 2020, 'Alternative', 12, 302.97),
('AL056', 'Boy Alone', 'Omah Lay', 'A056', 2023, 'Afrobeat', 12, 461.72),
('AL057', 'Wolfgang Amadeus Phoenix', 'Phoenix', 'A057', 2009, 'Indie Rock', 10, 53.36),
('AL058', 'Laurel Hell', 'Mitski', 'A058', 2022, 'Indie Rock', 11, 106.03),
('AL059', 'Nicole', 'NIKI', 'A059', 2022, 'R&B/Pop', 16, 32.16),
('AL060', 'Hey u x', 'BENEE', 'A060', 2020, 'Pop', 7, 169.41),
('AL061', 'Scorpion', 'Drake', 'A006', 2018, 'Hip-Hop', 25, 200.45),
('AL062', '÷', 'Ed Sheeran', 'A008', 2017, 'Pop', 16, 142.96),
('AL063', 'After Hours', 'The Weeknd', 'A009', 2020, 'R&B', 14, 416.08),
('AL064', 'Lust for Life', 'Lana Del Rey', 'A022', 2017, 'Indie Pop', 16, 184.81),
('AL065', 'Norman Fucking Rockwell!', 'Lana Del Rey', 'A022', 2019, 'Art Pop', 14, 147.66),
('AL066', 'DAMN.', 'Kendrick Lamar', 'A023', 2017, 'Hip-Hop', 14, 275.92),
('AL067', 'Astroworld', 'Travis Scott', 'A025', 2018, 'Hip-Hop', 17, 79.05),
('AL068', 'Melodrama', 'Lorde', 'A035', 2017, 'Electropop', 11, 403.08),
('AL069', 'Apricot Princess', 'Rex Orange County', 'A039', 2017, 'Indie Pop', 11, 46.53),
('AL070', 'The Kids Are Coming', 'Tones and I', 'A040', 2019, 'Pop', 7, 493.57),
('AL071', 'For Broken Ears', 'Tems', 'A033', 2020, 'R&B', 7, 388.4),
('AL072', 'Kala', 'M.I.A.', 'A048', 2007, 'Electronic', 12, 107.37),
('AL073', 'Gloria', 'Sam Smith', 'A049', 2023, 'Pop', 13, 12.71),
('AL074', 'Immunity', 'Clairo', 'A050', 2019, 'Indie Pop', 11, 409.58),
('AL075', 'Kid Krow', 'Conan Gray', 'A051', 2020, 'Indie Pop', 12, 356.36),
('AL076', 'Bewitched', 'Laufey', 'A052', 2023, 'Jazz Pop', 14, 367.21)]

mycursor.executemany(sqlFormula, albums)
mydb.commit()

mycursor.execute("CREATE TABLE ParentCompany (album_id VARCHAR(255), artist_name VARCHAR(255), release_date INT(255), parentCompany VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO ParentCompany (album_id, artist_name, release_date, parentCompany) VALUES (%s, %s, %s, %s)"

parentCompany = [('AL001', 'Taylor Swift', 2022, 'Universal Music Group'),
('AL002', 'Bad Bunny', 2022, 'Rimas Entertainment'),
('AL003', 'BTS', 2020, 'HYBE Corporation'),
('AL004', 'Billie Eilish', 2021, 'Universal Music Group'),
('AL005', 'Dua Lipa', 2020, 'Warner Music Group'),
('AL006', 'Drake', 2021, 'Universal Music Group'),
('AL007', 'Rosalía', 2022, 'Sony Music Entertainment'),
('AL008', 'Ed Sheeran', 2021, 'Warner Music Group'),
('AL009', 'The Weeknd', 2022, 'Universal Music Group'),
('AL010', 'Karol G', 2023, 'Universal Music Group'),
('AL011', 'SZA', 2022, 'Sony Music Entertainment'),
('AL012', 'Rema', 2022, 'Mavin Records'),
('AL013', 'Ice Spice', 2023, 'Universal Music Group'),
('AL014', 'Harry Styles', 2022, 'Sony Music Entertainment'),
('AL015', 'Olivia Rodrigo', 2023, 'Universal Music Group'),
('AL016', 'J Balvin', 2021, 'Universal Music Group'),
('AL017', 'Doja Cat', 2021, 'Sony Music Entertainment'),
('AL018', 'Shakira', 2017, 'Sony Music Entertainment'),
('AL019', 'Stray Kids', 2023, 'JYP Entertainment'),
('AL020', 'BLACKPINK', 2022, 'YG Entertainment'),
('AL021', 'Jung Kook', 2023, 'HYBE Corporation'),
('AL022', 'Lana Del Rey', 2023, 'Universal Music Group'),
('AL023', 'Kendrick Lamar', 2022, 'Universal Music Group'),
('AL024', 'Megan Thee Stallion', 2022, 'Warner Music Group'),
('AL025', 'Travis Scott', 2023, 'Sony Music Entertainment'),
('AL026', 'Peso Pluma', 2023, 'Double P Records'),
('AL027', 'Becky G', 2023, 'Sony Music Entertainment'),
('AL028', 'Riton', 2019, 'Sony Music Entertainment'),
('AL029', 'Arca', 2020, 'XL Recordings'),
('AL030', 'Anitta', 2022, 'Warner Music Group'),
('AL031', 'Fred again..', 2023, 'Warner Music Group'),
('AL032', 'Hozier', 2023, 'Sony Music Entertainment'),
('AL033', 'Tems', 2021, 'Sony Music Entertainment'),
('AL034', 'Sabrina Carpenter', 2022, 'Universal Music Group'),
('AL035', 'Lorde', 2021, 'Universal Music Group'),
('AL036', 'Stromae', 2022, 'Universal Music Group'),
('AL037', 'Grimes', 2020, 'Beggars Group'),
('AL038', 'Sevdaliza', 2020, 'Independent'),
('AL039', 'Rex Orange County', 2022, 'Sony Music Entertainment'),
('AL040', 'Tones and I', 2021, 'Independent'),
('AL041', 'RIT', 2023, 'Independent'),
('AL042', 'Kaytranada', 2019, 'Beggars Group'),
('AL043', 'Libianca', 2023, 'Warner Music Group'),
('AL044', 'Joy Crookes', 2022, 'Sony Music Entertainment'),
('AL045', 'Aminé', 2020, 'Independent'),
('AL046', 'Kali Uchis', 2018, 'Universal Music Group'),
('AL047', 'Mahalia', 2019, 'Warner Music Group'),
('AL048', 'M.I.A.', 2016, 'Beggars Group'),
('AL049', 'Sam Smith', 2020, 'Universal Music Group'),
('AL050', 'Clairo', 2021, 'Independent'),
('AL051', 'Conan Gray', 2022, 'Universal Music Group'),
('AL052', 'Laufey', 2023, 'Independent'),
('AL053', 'Tyla', 2023, 'Sony Music Entertainment'),
('AL054', 'Ice Cube', 1990, 'Universal Music Group'),
('AL055', 'Jean Dawson', 2020, 'Independent'),
('AL056', 'Omah Lay', 2023, 'Independent'),
('AL057', 'Phoenix', 2009, 'Independent'),
('AL058', 'Mitski', 2022, 'Independent'),
('AL059', 'NIKI', 2022, 'Independent'),
('AL060', 'BENEE', 2020, 'Universal Music Group'),
('AL061', 'Drake', 2018, 'Universal Music Group'),
('AL062', 'Ed Sheeran', 2017, 'Warner Music Group'),
('AL063', 'The Weeknd', 2020, 'Universal Music Group'),
('AL064', 'Lana Del Rey', 2017, 'Universal Music Group'),
('AL065', 'Lana Del Rey', 2019, 'Universal Music Group'),
('AL066', 'Kendrick Lamar', 2017, 'Universal Music Group'),
('AL067', 'Travis Scott', 2018, 'Sony Music Entertainment'),
('AL068', 'Lorde', 2017, 'Universal Music Group'),
('AL069', 'Rex Orange County', 2017, 'Sony Music Entertainment'),
('AL070', 'Tones and I', 2019, 'Independent'),
('AL071', 'Tems', 2020, 'Sony Music Entertainment'),
('AL072', 'M.I.A.', 2007, 'Beggars Group'),
('AL073', 'Sam Smith', 2023, 'Universal Music Group'),
('AL074', 'Clairo', 2019, 'Independent'),
('AL075', 'Conan Gray', 2020, 'Universal Music Group'),
('AL076', 'Laufey', 2023, 'Independent')]

mycursor.executemany(sqlFormula, parentCompany)
mydb.commit()



#1. Which parent company has the highest total revenue from all albums?
mycursor.execute("SELECT parentCompany, SUM(Albums.revenue) AS total_revenue FROM ParentCompany JOIN Albums ON ParentCompany.album_id = Albums.album_id GROUP BY parentCompany ORDER BY total_revenue DESC LIMIT 1")
for x in mycursor:
    print(x)

#2. Which album has the highest revenue?
mycursor.execute("SELECT album_name, revenue FROM Albums ORDER BY revenue DESC LIMIT 1")
for x in mycursor:
    print(x)

#3. Which album has the lowest revenue?
mycursor.execute("SELECT album_name, revenue FROM Albums ORDER BY revenue ASC LIMIT 1")
for x in mycursor:
    print(x)

#4. Which artist has the highest number of followers?
mycursor.execute("SELECT artist_name, followers FROM Artists ORDER BY followers DESC LIMIT 1")
for x in mycursor:
    print(x)

# 5. Which country has the highest number of artists?
mycursor.execute("SELECT country, COUNT(*) AS artist_count FROM Artists GROUP BY country ORDER BY artist_count DESC LIMIT 1")
for x in mycursor:
    print(x)

# 6. Which parent company has the highest number of artists?
mycursor.execute("SELECT parentCompany, COUNT(DISTINCT Artist) AS artist_count FROM ParentCompany GROUP BY parentCompany ORDER BY artist_count DESC LIMIT 1")
for x in mycursor:
    print(x)

# 7. Which genre has the highest number of listens?
mycursor.execute("SELECT genre, SUM(Listens) AS total_listens FROM Playlists GROUP BY genre ORDER BY total_listens DESC LIMIT 1")
for x in mycursor:
    print(x)