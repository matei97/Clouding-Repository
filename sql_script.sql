drop table Students
USE [Clouding]
GO

/****** Object:  Table [dbo].[Students]    Script Date: 3/14/2019 10:14:27 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Students](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[first_name] [varchar](50) NOT NULL,
	[last_name] [varchar](50) NOT NULL,
	[email] [varchar](100) NOT NULL,
	[added] [date] NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Students] ADD  CONSTRAINT [DF_Students_added]  DEFAULT (getdate()) FOR [added]
GO


insert into Students (first_name, last_name, email, added) values ('Jeanine', 'Samson', 'jsamson0@youku.com', '1/1/2019');
insert into Students (first_name, last_name, email, added) values ('Kimbra', 'Beswetherick', 'kbeswetherick1@infoseek.co.jp', '9/3/2018');
insert into Students (first_name, last_name, email, added) values ('Ervin', 'Luckings', 'eluckings2@comsenz.com', '1/29/2019');
insert into Students (first_name, last_name, email, added) values ('Dalli', 'Flanagan', 'dflanagan3@tripod.com', '9/4/2018');
insert into Students (first_name, last_name, email, added) values ('Nappy', 'Josephoff', 'njosephoff4@apache.org', '6/9/2018');
insert into Students (first_name, last_name, email, added) values ('Gretal', 'Iannazzi', 'giannazzi5@sphinn.com', '10/16/2018');
insert into Students (first_name, last_name, email, added) values ('Leeanne', 'Leeuwerink', 'lleeuwerink6@qq.com', '7/30/2018');
insert into Students (first_name, last_name, email, added) values ('Dar', 'Bygott', 'dbygott7@howstuffworks.com', '10/24/2018');
insert into Students (first_name, last_name, email, added) values ('Dee', 'Melpuss', 'dmelpuss8@constantcontact.com', '11/19/2018');
insert into Students (first_name, last_name, email, added) values ('Katrinka', 'Hamman', 'khamman9@uiuc.edu', '10/16/2018');
insert into Students (first_name, last_name, email, added) values ('Trev', 'Fendlen', 'tfendlena@marketwatch.com', '10/25/2018');
insert into Students (first_name, last_name, email, added) values ('Boniface', 'Jedrzejczyk', 'bjedrzejczykb@amazonaws.com', '4/27/2018');
insert into Students (first_name, last_name, email, added) values ('Dyann', 'Borne', 'dbornec@harvard.edu', '10/16/2018');
insert into Students (first_name, last_name, email, added) values ('Geneva', 'Gumbley', 'ggumbleyd@google.nl', '9/3/2018');
insert into Students (first_name, last_name, email, added) values ('Teirtza', 'Meron', 'tmerone@wsj.com', '4/11/2018');
insert into Students (first_name, last_name, email, added) values ('Gabey', 'Connop', 'gconnopf@comcast.net', '12/18/2018');
insert into Students (first_name, last_name, email, added) values ('Hort', 'Gwatkin', 'hgwatking@narod.ru', '11/11/2018');
insert into Students (first_name, last_name, email, added) values ('Vin', 'Cleworth', 'vcleworthh@hibu.com', '1/2/2019');
insert into Students (first_name, last_name, email, added) values ('Diane-marie', 'Robel', 'drobeli@vimeo.com', '9/3/2018');
insert into Students (first_name, last_name, email, added) values ('Gretta', 'Bowller', 'gbowllerj@cornell.edu', '9/22/2018');
insert into Students (first_name, last_name, email, added) values ('Tildie', 'Petriello', 'tpetriellok@indiegogo.com', '2/6/2019');
insert into Students (first_name, last_name, email, added) values ('Karlene', 'Meran', 'kmeranl@hud.gov', '3/13/2018');
insert into Students (first_name, last_name, email, added) values ('Gerik', 'Haggith', 'ghaggithm@craigslist.org', '4/3/2018');
insert into Students (first_name, last_name, email, added) values ('Shandra', 'Bryett', 'sbryettn@gov.uk', '1/28/2019');
insert into Students (first_name, last_name, email, added) values ('Sam', 'Keynd', 'skeyndo@istockphoto.com', '1/29/2019');
insert into Students (first_name, last_name, email, added) values ('Putnem', 'Von Welldun', 'pvonwelldunp@shutterfly.com', '11/4/2018');
insert into Students (first_name, last_name, email, added) values ('Saidee', 'Jiggen', 'sjiggenq@earthlink.net', '10/30/2018');
insert into Students (first_name, last_name, email, added) values ('Archy', 'Oxer', 'aoxerr@wordpress.com', '8/14/2018');
insert into Students (first_name, last_name, email, added) values ('Barnie', 'Putman', 'bputmans@pbs.org', '8/25/2018');
insert into Students (first_name, last_name, email, added) values ('Esra', 'Ingman', 'eingmant@themeforest.net', '6/1/2018');
insert into Students (first_name, last_name, email, added) values ('Felipe', 'Trussman', 'ftrussmanu@yahoo.co.jp', '10/15/2018');
insert into Students (first_name, last_name, email, added) values ('Sigismondo', 'Olifard', 'solifardv@ovh.net', '12/2/2018');
insert into Students (first_name, last_name, email, added) values ('Angie', 'Cadalleder', 'acadallederw@independent.co.uk', '1/27/2019');
insert into Students (first_name, last_name, email, added) values ('Casey', 'Nicolls', 'cnicollsx@oaic.gov.au', '5/5/2018');
insert into Students (first_name, last_name, email, added) values ('Robers', 'Cullon', 'rcullony@cnbc.com', '10/31/2018');
insert into Students (first_name, last_name, email, added) values ('Christye', 'Danev', 'cdanevz@webnode.com', '3/27/2018');
insert into Students (first_name, last_name, email, added) values ('Alta', 'Valler', 'avaller10@un.org', '2/14/2019');
insert into Students (first_name, last_name, email, added) values ('Brooks', 'Vynehall', 'bvynehall11@examiner.com', '1/28/2019');
insert into Students (first_name, last_name, email, added) values ('Lilian', 'Howgego', 'lhowgego12@indiatimes.com', '12/22/2018');
insert into Students (first_name, last_name, email, added) values ('Moyna', 'Sentinella', 'msentinella13@ebay.com', '10/11/2018');
insert into Students (first_name, last_name, email, added) values ('Lilias', 'Thornewill', 'lthornewill14@ask.com', '2/11/2019');
insert into Students (first_name, last_name, email, added) values ('Quinn', 'Loughan', 'qloughan15@barnesandnoble.com', '7/4/2018');
insert into Students (first_name, last_name, email, added) values ('Julio', 'Wildbore', 'jwildbore16@twitter.com', '2/5/2019');
insert into Students (first_name, last_name, email, added) values ('Brucie', 'Garrity', 'bgarrity17@surveymonkey.com', '8/9/2018');
insert into Students (first_name, last_name, email, added) values ('Nada', 'Wank', 'nwank18@zimbio.com', '11/7/2018');
insert into Students (first_name, last_name, email, added) values ('Ashbey', 'Aldam', 'aaldam19@tripadvisor.com', '4/19/2018');
insert into Students (first_name, last_name, email, added) values ('Jenica', 'Hast', 'jhast1a@tiny.cc', '6/12/2018');
insert into Students (first_name, last_name, email, added) values ('Wilona', 'Ingon', 'wingon1b@hc360.com', '12/27/2018');
insert into Students (first_name, last_name, email, added) values ('Dannie', 'Antonutti', 'dantonutti1c@usnews.com', '12/9/2018');
insert into Students (first_name, last_name, email, added) values ('Ringo', 'Escott', 'rescott1d@hatena.ne.jp', '12/16/2018');
insert into Students (first_name, last_name, email, added) values ('Mack', 'Minshall', 'mminshall1e@tuttocitta.it', '8/27/2018');
insert into Students (first_name, last_name, email, added) values ('Rupert', 'Amys', 'ramys1f@fotki.com', '3/17/2018');
insert into Students (first_name, last_name, email, added) values ('Leicester', 'Arendsen', 'larendsen1g@techcrunch.com', '7/29/2018');
insert into Students (first_name, last_name, email, added) values ('Nert', 'Syversen', 'nsyversen1h@twitpic.com', '4/9/2018');
insert into Students (first_name, last_name, email, added) values ('Biron', 'Fellows', 'bfellows1i@ehow.com', '8/15/2018');
insert into Students (first_name, last_name, email, added) values ('Drucie', 'Putterill', 'dputterill1j@i2i.jp', '3/18/2018');
insert into Students (first_name, last_name, email, added) values ('Goober', 'MacGaughy', 'gmacgaughy1k@ehow.com', '6/2/2018');
insert into Students (first_name, last_name, email, added) values ('Alexis', 'Briston', 'abriston1l@utexas.edu', '5/17/2018');
insert into Students (first_name, last_name, email, added) values ('Loreen', 'Nesbeth', 'lnesbeth1m@nature.com', '2/23/2019');
insert into Students (first_name, last_name, email, added) values ('Jami', 'Abramowsky', 'jabramowsky1n@photobucket.com', '4/3/2018');
insert into Students (first_name, last_name, email, added) values ('Olivier', 'Eixenberger', 'oeixenberger1o@example.com', '2/17/2019');
insert into Students (first_name, last_name, email, added) values ('Amil', 'Tidey', 'atidey1p@merriam-webster.com', '7/16/2018');
insert into Students (first_name, last_name, email, added) values ('Shirl', 'Rentoll', 'srentoll1q@ustream.tv', '4/6/2018');
insert into Students (first_name, last_name, email, added) values ('Cecile', 'Bakesef', 'cbakesef1r@people.com.cn', '3/24/2018');
insert into Students (first_name, last_name, email, added) values ('Kristy', 'Francklin', 'kfrancklin1s@pen.io', '11/5/2018');
insert into Students (first_name, last_name, email, added) values ('Robbin', 'Yearron', 'ryearron1t@imageshack.us', '5/26/2018');
insert into Students (first_name, last_name, email, added) values ('Vern', 'Awmack', 'vawmack1u@toplist.cz', '9/30/2018');
insert into Students (first_name, last_name, email, added) values ('Sarita', 'Leaf', 'sleaf1v@cbsnews.com', '8/13/2018');
insert into Students (first_name, last_name, email, added) values ('Dominique', 'Hazlegrove', 'dhazlegrove1w@abc.net.au', '12/7/2018');
insert into Students (first_name, last_name, email, added) values ('Eolande', 'Woodhouse', 'ewoodhouse1x@blogs.com', '1/25/2019');
insert into Students (first_name, last_name, email, added) values ('Chick', 'Cucuzza', 'ccucuzza1y@i2i.jp', '6/20/2018');
insert into Students (first_name, last_name, email, added) values ('Illa', 'Zottoli', 'izottoli1z@bloglines.com', '4/14/2018');
insert into Students (first_name, last_name, email, added) values ('Paul', 'McKevin', 'pmckevin20@deviantart.com', '12/5/2018');
insert into Students (first_name, last_name, email, added) values ('Vito', 'Clabburn', 'vclabburn21@comcast.net', '11/21/2018');
insert into Students (first_name, last_name, email, added) values ('Christian', 'Odney', 'codney22@goo.ne.jp', '7/11/2018');
insert into Students (first_name, last_name, email, added) values ('Albie', 'Gillibrand', 'agillibrand23@vkontakte.ru', '10/3/2018');
insert into Students (first_name, last_name, email, added) values ('Dorise', 'Semerad', 'dsemerad24@who.int', '10/19/2018');
insert into Students (first_name, last_name, email, added) values ('Sterne', 'Hebborne', 'shebborne25@google.nl', '12/19/2018');
insert into Students (first_name, last_name, email, added) values ('Justis', 'Jeppensen', 'jjeppensen26@dion.ne.jp', '3/6/2019');
insert into Students (first_name, last_name, email, added) values ('Lotte', 'Marshallsay', 'lmarshallsay27@archive.org', '10/3/2018');
insert into Students (first_name, last_name, email, added) values ('Nesta', 'Hengoed', 'nhengoed28@buzzfeed.com', '3/7/2019');
insert into Students (first_name, last_name, email, added) values ('Izak', 'Burnsides', 'iburnsides29@hao123.com', '9/15/2018');
insert into Students (first_name, last_name, email, added) values ('Freddie', 'Boulden', 'fboulden2a@ihg.com', '6/21/2018');
insert into Students (first_name, last_name, email, added) values ('Tadd', 'Garz', 'tgarz2b@theatlantic.com', '8/3/2018');
insert into Students (first_name, last_name, email, added) values ('Darius', 'MacLoughlin', 'dmacloughlin2c@tinyurl.com', '2/2/2019');
insert into Students (first_name, last_name, email, added) values ('Lolly', 'Climar', 'lclimar2d@tripod.com', '11/27/2018');
insert into Students (first_name, last_name, email, added) values ('Gwendolen', 'Verna', 'gverna2e@friendfeed.com', '4/5/2018');
insert into Students (first_name, last_name, email, added) values ('Diarmid', 'Poulney', 'dpoulney2f@scribd.com', '2/10/2019');
insert into Students (first_name, last_name, email, added) values ('Hadlee', 'Organer', 'horganer2g@nps.gov', '1/15/2019');
insert into Students (first_name, last_name, email, added) values ('Tiebold', 'Sallter', 'tsallter2h@infoseek.co.jp', '6/3/2018');
insert into Students (first_name, last_name, email, added) values ('Nicolas', 'Lanfer', 'nlanfer2i@edublogs.org', '3/8/2019');
insert into Students (first_name, last_name, email, added) values ('Normie', 'Tremethack', 'ntremethack2j@unblog.fr', '3/7/2019');
insert into Students (first_name, last_name, email, added) values ('Tull', 'Piegrome', 'tpiegrome2k@yahoo.com', '2/9/2019');
insert into Students (first_name, last_name, email, added) values ('Kelvin', 'Andreasen', 'kandreasen2l@woothemes.com', '7/14/2018');
insert into Students (first_name, last_name, email, added) values ('Nathalie', 'Elstub', 'nelstub2m@hc360.com', '3/7/2019');
insert into Students (first_name, last_name, email, added) values ('Tiena', 'Edgcumbe', 'tedgcumbe2n@ibm.com', '2/5/2019');
insert into Students (first_name, last_name, email, added) values ('Stanislaus', 'Cana', 'scana2o@domainmarket.com', '1/26/2019');
insert into Students (first_name, last_name, email, added) values ('Maximilien', 'Gleaves', 'mgleaves2p@weibo.com', '6/16/2018');
insert into Students (first_name, last_name, email, added) values ('Eugine', 'Playle', 'eplayle2q@weibo.com', '6/19/2018');
insert into Students (first_name, last_name, email, added) values ('Gav', 'Burburough', 'gburburough2r@hexun.com', '11/6/2018');
