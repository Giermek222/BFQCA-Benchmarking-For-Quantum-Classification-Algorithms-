create table algorithm (
                           id int not null identity,
                           algorithmName varchar(30) not null,
                           problemName varchar(100) not null,
                           author varchar(50) not null,
                           algorithmDescription varchar(100),
                           constraint algorithm_pk primary key (id)
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
                           algorithm_name varchar(30) not null,
                           problem_name varchar(30) not null,
                           training_accuracy numeric(9,3),
                           training_precision numeric(9,3),
                           training_recall numeric(9,3),
                           training_f1_score numeric(9,3),
                           training_loss numeric(9,3),
                           test_accuracy numeric(9,3),
                           test_precision numeric(9,3),
                           test_recall numeric(9,3),
                           test_f1_score numeric(9,3),
                           test_loss numeric(9,3),
                           max_latency_ms numeric(9,3),
                           min_latency_ms numeric(9,3),
                           avg_latency_ms numeric(9,3),
                           percentile_latency_ms numeric(9,3),
                           time numeric(18,3),
                           constraint benchmark_pk primary key (id)
);

create table dataset (
    id int not null identity,
    problemName varchar(30) not null
);
