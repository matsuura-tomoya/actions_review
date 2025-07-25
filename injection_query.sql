CREATE OR REPLACE PROCEDURE get_employees_unsafe(DEPT_NAME VARCHAR)
RETURNS TABLE(name VARCHAR, email VARCHAR)
LANGUAGE JAVASCRIPT
AS
$$
    // ユーザーからの入力を直接SQL文に連結している（危険！）
    var sql_command = "SELECT name, email FROM public.employees WHERE department = '" + DEPT_NAME + "';";

    var stmt = snowflake.createStatement({sqlText: sql_command});
    var result = stmt.execute();
    return result;
$$;