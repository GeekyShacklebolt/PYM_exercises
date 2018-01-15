import click
import pkg_resources

ver = pkg_resources.require("myhello")[0].version

@click.command()
@click.option('--verbose', '-V', is_flag=True, help="Will print verbose message.")
@click.option('--version', '-v', is_flag=True, help="Will print the current version of the application.")
@click.option('--name', '-n', multiple=True, default='', help="Enter your name.")
@click.argument('Country')  # this is a must have argument
@click.password_option()
def cli(verbose, version, name, password, country):
    """This is an example script, while learning click for creating 
       command line applications."""
    if verbose:
        click.echo("This is my first command line application using click.")
    elif version:
        click.echo("Version: {0}".format(ver))
    
    click.echo("Hello {0}!".format(country))
    for i in name:
        click.echo("Bye {0}".format(i))
    click.echo("Password is successfully accepted.")
    # click.echo("We reveived {0} as password.".format(password))
    # ECHOING PASSWORD WASN'T RECOMMENDED!   
