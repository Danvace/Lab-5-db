CREATE table if not EXISTS update_log
(
    id         int       not null auto_increment,
    row_id     int       not null,
    updated_at timestamp not null default current_timestamp,
    primary key (id)
);

DELIMITER //
CREATE trigger update_log_trigger
    after update
    on review
    for each row
begin
    insert into update_log (row_id) values (new.id);
end //

DELIMITER ;

update review set response = 'testasdgsg' where id = 11;