create table algorithm (
                           id int not null identity,
                           algorithmName varchar(30) not null,
                           problemName varchar(100) not null,
                           algorithmDescription varchar(100),
                           constraint algorithm_pk primary key (id),
);

create table users (
                      id int not null identity ,
                      userName varchar(30) not null,
                      password varchar(100) not null,
                      token varchar(20),
                      constraint users_pk primary key (id)
);

create table benchmark (
                           id int not null identity ,
                           algorithmName varchar(30) not null,
                           problemName varchar(30) not null,
                           accuracyLearning numeric(9,3),
                           accuracyTest numeric(9,3),
                           lossTest numeric(9,3),
                           lossLearning numeric(9,3),
                           maxLatency numeric(9,3),
                           minLatency numeric(9,3),
                           avgLatency numeric(9,3),
                           latencyPercentile numeric(9,3),
                           time numeric(9,3),
                           constraint benchmark_pk primary key (id)
);
