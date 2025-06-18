from jinja2 import Environment, FileSystemLoader


def print_html(person):
    """Печать отчета."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("report.html")
    context = []

    with open('report.html', mode="w", encoding="utf-8") as message:
        for key in person:
            line = person[key]
            context.append(line)
        content = template.render(
            context = context
        )
        message.write(content)

def print_html_team(person):
    """Печать отчета по командам."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("report_team.html")
    context = []

    with open('report.html', mode="w", encoding="utf-8") as message:
        team_data = {}
        team_list = []
        for key in person:
            # раскидал по коллективам
            total_person = person[key]
            if total_person['organization_id'] in team_data:
                team_data[total_person['organization_id']].append(total_person)
            else:
                team_data[total_person['organization_id']] = [total_person]
                team_list.append(total_person['organization_id'])
        context.append(team_data)
        content = template.render(
            context = context,
            team_list = team_list
        )
        message.write(content)






