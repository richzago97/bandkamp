quantas musicas podem ter em um album? muitos
quantos albuns podem ter em uma musica? um

quantos usuarios podem ter/cadastrar uma canção? muitos
quantas canções podem ter/cadastrados em um usuario? muitos

quantos usuarios podem ter/cadastrar um album? muitos 
quantos albuns podem ter /ser/cadastrados por/um usuario? muitos
Table User {
  id int
  first_name varchar
  last_name varchar
  
  Indexes {
    (id) [pk]
  }
}

Table Song {
  id int
  title varchar(255)
  duration varchar(255)
  
  Indexes {
    (id) [pk]
  }
}

Ref: public.Song.id < public.Album.id
Ref: public.User.id <> public.Album.id
Ref: public.User.id <> public.Song.id

Table Album {
  id int
  name varchar(255)
  year integer
  
   Indexes {
    (id) [pk]
  }
}
