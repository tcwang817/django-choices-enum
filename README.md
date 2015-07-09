django-choices-enum
===================

django-choices-enum allows the usage of the 2.x backport of Python 3.4's enum
package (enum34) as choices in Django models.

    from django.db import models
    from django_choices_enum import ChoicesEnum

    class Monster(models.Model):
        class Types(str, ChoicesEnum):
            BEAST = ('beast', 'Beast')
            UNDEAD = ('undead', 'Undead')
            HUMAN = ('human', 'Human')

        name = models.CharField(max_length=40)
        type = models.CharField(max_length=40, choices=Types.choices())

You may now write code like this:

    monsters = Monster.objects.filter(type=Monster.Types.BEAST)
    for m in monsters:
        assert m.type == Monster.Types.BEAST

    m = Monster(name='Vampire', type=Monster.Types.UNDEAD)
    m.save()

Details
=======

Each enumeration is a class subclassed from the type of the field and the
ChoicesEnum type:

    class MyIntEnumeration(int, ChoicesEnum):
        A = (1, 'Label A')

Each constant is then assigned a tuple of (value, label) as expected by
the Django choices parameter.  If the constant and label are the same,
you may omit the tuple and simply set the constant equal to the value of
the choice.

Contributions
=============

I did not really write most of this code.  It was found and fixed from
a Gist:

https://gist.github.com/dstufft/5600529
