#1-Performance des employés : volume & qualité
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(Nom, Prenom, nbr_commandes_livrees)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import matplotlib.pyplot as plt
dataset['Employé'] = dataset['Prenom'] + " " + dataset['Nom']
dataset['Total'] = dataset['nbr_commandes_livrees'] + dataset['nbr_commandes_non_livrees']
dataset = dataset.groupby('Employé', as_index=False).sum()
dataset = dataset.sort_values('Total', ascending=False).head(8)
plt.figure(figsize=(9,4))
plt.barh(dataset['Employé'], dataset['nbr_commandes_livrees'], label='Livrées',color='#B0E0E6')
plt.barh(dataset['Employé'], dataset['nbr_commandes_non_livrees'],
         left=dataset['nbr_commandes_livrees'], label='Non livrées',color='#EDF2FB')
plt.gca().invert_yaxis()
plt.title("Performance des employés : volume & qualité")
plt.xlabel("Nombre de commandes")
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.show()

#_____________________________________________________________________________________________________

#2-Répartition des clients à risque\n(Commandes non livrées
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(CompanyName, nbr_commandes_non_livrees)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import matplotlib.pyplot as plt
dataset = dataset.groupby('CompanyName', as_index=False)['nbr_commandes_non_livrees'].sum()
dataset = dataset.sort_values('nbr_commandes_non_livrees', ascending=False).head(6)
values = dataset['nbr_commandes_non_livrees']
labels = dataset['CompanyName']
colors = ['#4C72B0', '#6BAED6', '#9ECAE1', '#C6DBEF', '#D9EAF7', '#EDF2FB']

plt.figure(figsize=(6,6))
plt.pie(
    values,
    labels=labels,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%'
)
plt.title("Répartition des clients à risque\n(Commandes non livrées)", fontsize=11)
plt.tight_layout()
plt.show()


#_____________________________________________________________________________________________________


#3-Tendance des livraisons dans le temps
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(mois_annee, nbr_commandes_livrees, nbr_commandes_non_livrees)
# dataset = dataset.drop_duplicates()
# Collez ou tapez votre code de script ici :
import matplotlib.pyplot as plt
dataset = dataset.groupby('mois_annee', as_index=False).sum()
dataset = dataset.sort_values('mois_annee')
plt.figure(figsize=(11,4))
plt.plot(dataset['mois_annee'], dataset['nbr_commandes_livrees'],
         label='Livrées', linewidth=2, color='#B0E0E6')
plt.plot(dataset['mois_annee'], dataset['nbr_commandes_non_livrees'],
         label='Non livrées', linewidth=2, color='#8172B3')
plt.title("Tendance des livraisons dans le temps")
plt.ylabel("Nombre de commandes")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()


#_____________________________________________________________________________________________________


#4-Répartition des commandes
# Le code suivant, qui crée un dataframe et supprime les lignes dupliquées, est toujours exécuté et sert de préambule à votre script : 

# dataset = pandas.DataFrame(nbr_commandes_livrees, nbr_commandes_non_livrees)
# dataset = dataset.drop_duplicates()

# Collez ou tapez votre code de script ici :
import matplotlib.pyplot as plt
livrees = dataset['nbr_commandes_livrees'].sum()
non_livrees = dataset['nbr_commandes_non_livrees'].sum()
values = [livrees, non_livrees]
labels = ['Livrées', 'Non livrées']
colors = ['powderblue', '#D9EAF7']
plt.figure(figsize=(4,4))
plt.pie(
    values,
    labels=labels,
    colors=colors,
    startangle=90,
    autopct='%1.1f%%',
    wedgeprops=dict(width=0.4)
)
plt.title("Répartition des commandes")
plt.tight_layout()
plt.show()