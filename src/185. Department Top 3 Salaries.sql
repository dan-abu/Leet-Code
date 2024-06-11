-- Question can be found using this link: https://leetcode.com/problems/department-top-three-salaries/
-- Solution below
with salary_rank as (
    select
        e.id
        , e.departmentId
        , d.name Department
        , e.name Employee
        , e.salary
        , dense_rank() over (partition by d.name order by e.salary desc) salary_rank
    from Employee e
    join Department d on d.id = e.departmentId
)
select
    Department,
    Employee,
    Salary
from salary_rank
where salary_rank < 4;