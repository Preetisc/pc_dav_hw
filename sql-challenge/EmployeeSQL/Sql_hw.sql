--1. List the following details of each employee: employee number, last name, first name, gender, and salary.

select e.emp_no,first_name,last_name,gender,salary from employees e,salaries s where e.emp_no=s.emp_no

--2. List employees who were hired in 1986.
select * from employees where hire_date >= '1986-01-01' order by hire_date

--3. List the manager of each department with the following information: department number, department name, 
--the manager's employee number, last name, first name, and start and end employment dates.

Select d.dept_no,d.dept_name,dm.from_date, dm.to_date,dm.emp_no,e.first_name,e.last_name from  departments d 
join dept_manager  dm on dm.dept_no=d.dept_no
join employees e on e.emp_no = dm.emp_no

--4. List the department of each employee with the following information: employee number, last name, first name, and department name.
select e.emp_no ,e.first_name, e.last_name, dm.dept_no,d.dept_name from employees e
Join public.dept_manager dm on dm.emp_no=e.emp_no
join public.departments d on d.dept_no=dm.dept_no


--5. List all employees whose first name is "Hercules" and last names begin with "B."
Select * from employees where first_name='Hercules' and last_name like 'B%' 

--6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

Select e.emp_no,e.first_name,e.last_name,d.dept_name from employees e 
join dept_emp de on de.emp_no =e.emp_no
join departments d on d.dept_no=de.dept_no
where d.dept_name ='Sales'


--7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
Select e.emp_no,e.first_name,e.last_name,d.dept_name from employees e 
join dept_emp de on de.emp_no =e.emp_no
join departments d on d.dept_no=de.dept_no
where d.dept_name in ('Sales','Development')
					  
--8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(*) as same_last_name from employees group by last_name order by same_last_name desc