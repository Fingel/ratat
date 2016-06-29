RAT Account Tabulator
=====================

Setup:

1. Create a virtualenv and source it: `virtualenv env/ && source env/bin/activate`
2. Install the requirements: `pip install -r requirements.txt`
3. Run the migratoins: `./manage.py migrate`
4. Create a superuser: `./manage.py createsuperuser`
5. Launch the dev server: `./manage.py runserver`
6. Visit the admin site: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin)
7. Create some classes, races and players.
8. Check out the console: `./manage.py shell_plus`
9. Profit


A few things you can try in the console (step 8):


    In [1]: c = Character.objects.first()

    In [2]: c.race
    Out[2]: <Race: Human>

    In [3]: c.dass
    Out[3]: <Dass: Warrior>

    In [4]: c.wis
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-4-a219aaebeb37> in <module>()
    ----> 1 c.wis

    AttributeError: 'Character' object has no attribute 'wis'

    In [5]: c.wit
    Out[5]: 11
