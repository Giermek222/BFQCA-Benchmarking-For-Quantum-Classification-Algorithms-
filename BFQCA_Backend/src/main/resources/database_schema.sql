create table algorithm (
                           id int not null AUTO_INCREMENT,
                           algorithmName varchar(30) not null,
                           problemName varchar(100) not null,
                           algorithmDescription varchar(100),
                           constraint algorithm_pk primary key (id),
                           constraint algorithm_uk unique key (algorithmName)
) engine = INNODB;

create table user (
                      id int not null AUTO_INCREMENT,
                      userName varchar(30) not null,
                      password varchar(100) not null,
                      token varchar(20),
                      constraint algorithm_pk primary key (id)
) engine = INNODB;

create table benchmark (
                           id int not null AUTO_INCREMENT,
                           algorithmName varchar(30) not null,
                           problemName varchar(30) not null,
                           accuracyLearning double,
                           accuracyTest double,
                           lossTest double,
                           lossLearning double,
                           maxLatency double,
                           minLatency double,
                           avgLatency double,
                           latencyPercentile double,
                           time double,
                           constraint algorithm_pk primary key (id)
) engine = INNODB;
