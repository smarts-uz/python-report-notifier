import click

# Initialize an empty list to store items
items = []

@click.command()
@click.argument('new_item', type=str)
def add_item(new_item):
    """Add a new item to the list."""
    items.append(new_item)
    click.echo(f'Item "{new_item}" added successfully!')

@click.command()
def show_list():
    """Show the current list of items."""
    if not items:
        click.echo('The list is empty.')
    else:
        click.echo('Current list of items:')
        for item in items:
            click.echo(f'- {item}')

# Create a Click Group to group the commands
@click.group()
def cli():
    """Simple CLI app to manage a list of items."""
    pass

# Add the commands to the Click Group
cli.add_command(add_item)
cli.add_command(show_list)

# Entry point for the CLI
if __name__ == '__main__':
    cli()