from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from smartmedix.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SmartmedixCrew():
	"""Smartmedix crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def fitness_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['fitness_expert'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def nutritionist(self) -> Agent:
		return Agent(
			config=self.agents_config['nutritionist'],
			verbose=True
		)

	@agent
	def doctor(self) -> Agent:
		return Agent(
			config=self.agents_config['doctor'],
			verbose=True
		)

	@agent
	def disease_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['disease_expert'],
			verbose=True
		)

	@task
	def fitness_task(self) -> Task:
		return Task(
			config=self.tasks_config['fitness_task'],
			agent=self.fitness_expert()
		)

	@task
	def nutrition_task(self) -> Task:
		return Task(
			config=self.tasks_config['nutrition_task'],
			agent=self.nutritionist(),
		)

	@task
	def healthanalysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['healthanalysis_task'],
			agent=self.doctor(),
		)

	@task
	def disease_task(self) -> Task:
		return Task(
			config=self.tasks_config['disease_task'],
			agent=self.disease_expert(),
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Smartmedix crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)