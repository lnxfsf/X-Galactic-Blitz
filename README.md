# X-Galactic-Blitz
X-Galactic-Blitz: Defending Earth with SpaceX



U `develop` branch ide, pre no u `main`.

svaka grupica, u svoj branch .. 

---------
### Ko je u koju grupicu: 
```
group1 - igor lerinc

group2 - 

group3 - 
```




-----------


# Guidelines for project
Ovo su guidelines, kojeg se drzimo, da bi bilo consistent i čitljivo, pridržavaj se toga .. 


Samo ja (igor) merge-ujem u `main` kao finalni working kod (kada se neki feature do kraja doradi.. pa moze safely da se ubaci.. )

prvo proveri da li radi u vas branch kako treba ta funkcionalnost;
koristite vaš `develop-group#` u koji testirate sve funkcionalnosti da radi kako treba (u koji i VI rešite merge conflicts ako ima neki), i onda mozete poslati u `develop` branch, u slucaju da radi sve (ako sve radi, bice odma i approved.. samo da nema merge conflict koji ja moram da rešavam, kada VI treba to unapred da rešite.. u vaš `develop-group#` ...  )
ako radi, šalješ `develop` branch, za koji takođe need approval for pull request by me :) ( u `develop` branch, se jos jednom proveri, da sve funkcionalnosti (na kojima radiš) rade kako treba i ako rade, ubaci se u `main` ako je funkcionalnost dorađena do kraja, ako nije dorađena do kraja, ostaje u `develop` dok se ne doradi do kraja.. )



### Commit Related Changes
A commit should be a wrapper for related changes. For example, fixing two different bugs should produce two separate commits. Small commits make it easier for other developers to understand the changes and roll them back if something went wrong.
With tools like the staging area and the ability to stage only parts of a file, Git makes it easy to create very granular commits.
	
### Commit Often
Committing often keeps your commits small and, again, helps you commit only related changes. Moreover, it allows you to share your code more frequently with others. That way it‘s easier for everyone to integrate changes regularly and avoid having merge conflicts. Having large commits and sharing them infrequently, in contrast, makes it hard to solve conflicts.

### Don't Commit Half-Done Work
You should only commit code when a logical component is completed.
Split a feature‘s implementation into logical chunks that can be completed quickly so that you can commit often. If you‘re tempted to commit just because you need a clean working copy (to check out a branch, pull in changes, etc.) consider using Git‘s «Stash» feature instead.

### Test Your Code Before You Commit
Resist the temptation to commit something that you «think» is completed. Test it thoroughly to make sure it really is completed and has no side effects (as far as one can tell). While committing half-baked things in your local repository only requires you to forgive yourself, having your code tested is even more important when it comes to pushing/sharing your code with others.

### Write Good Commit Messages
Begin your message with a short summary of your changes (up to 50 characters as a guideline). Separate it from
the following body by including a blank line. The body of your message should provide detailed answers to the following questions:
– What was the motivation for the change? – How does it differ from the previous
implementation?
Use the imperative, present tense («change», not «changed» or «changes») to be consistent with generated messages from commands like git merge.
Having your files backed up on a remote server is a nice side effect of having a version control system. But you should not use your VCS like it was a backup system. When doing version control, you should pay attention to committing semantically (see «related changes») - you shouldn‘t just cram in files.


### Use Branches
Branching is one of Git‘s most powerful features - and this is not by accident: quick and easy branching was a central requirement from day one. Branches are the perfect tool to help you avoid mixing up different lines of development. You should use branches extensively in your development workflows: for new features, bug fixes, ideas...



## Formatting Rules

- Prvo slovo veliko, za summary message

- __Always leave the second line blank.__  znači počinješ od 3 linije da pišeš long description..

zato što: first line (which is the commit title (summary message)), and actual commit message is on the third line.
Evo [vidi](https://imgur.com/shMknul.png) i to izgleda [readable](https://imgur.com/Xzqo3ya.png)

- I koristi description as bullet points:
```
  commit ae878fc8b9761d099a4145617e4a48cbeb390623
  Author: [removed]
  Date:   Fri Jun 1 01:44:02 2012 +0000

    Refactor libvirt create calls

     - Minimize duplicated code for create

     - Make wait_for_destroy happen on shutdown instead of undefine

     - Allow for destruction of an instance while leaving the domain
```



## Issues
Ovo je jako vazno. 
U [issues](https://github.com/Linuxiness/X-Galactic-Blitz/issues), svaka grupica ima svoj broj za labels (labels za issues koristi) (grupica 1 je broj 1 , grupica 2 je broj 2, grupica 3 je broj 3 ),
i tu treba u okviru vaše grupice, da stavljate sve u vezi vašeg dijela posla. bugs, TODO, želje, features, itd.. 

Labels bez broja, vazi za cijeli program, van vašeg dijela posla, koji treba ili zajednički effort, ili neko drugi u okviru naše grupe, da odradi.. (tu mozes ubaciti feature improvements i slicno.. da to bude dokumentovano ... )


## Milestones
Takođe, ako oćeš, koristi [Milestones](https://github.com/Linuxiness/X-Galactic-Blitz/milestones), da lakse organizujes issues na kojima radis trenutno. 
I time je to kao tracker, kolko je odrađeno.. i kada i šta.. 

---------------------------------

References: 
[Git](https://quickref.me/git)



---------------------------------

hello



