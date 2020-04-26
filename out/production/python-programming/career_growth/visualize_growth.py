from src.career_growth.graph import Graph


# importing the required module


def visualize(year: [], salary: []):
    graph = Graph(year, salary)
    graph.draw_graph("Gagan Salary", "year", "salary (x 100,000 INR)")


def main():
    salaries = {2010: 3.16, 2011: 3.6,
                2012: 4.2, 2013: 8, 2014: 9, 2014.5: 14,
                2016: 18, 2016.5: 26}
    x, y = zip(*sorted(salaries.items()))
    visualize(x, y);


if __name__ == "__main__":
    main()
