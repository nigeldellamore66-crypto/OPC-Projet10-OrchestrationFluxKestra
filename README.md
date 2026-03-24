# Pipeline d'orchestration de données — Bottleneck (Kestra)

> Automatisation complète du traitement, de la fusion et de l'analyse de données
> commerciales multi-sources pour générer des rapports de chiffre d'affaires,
> en utilisant Kestra comme orchestrateur.

## Contexte & objectif

L'entreprise Bottleneck reçoit des données de ventes depuis plusieurs sources
hétérogènes (ERP, Web, fichiers de liaison). Ce projet automatise entièrement :
- le nettoyage et la dédoublonnage de ces fichiers
- leur fusion en une source unifiée
- la classification des vins et le calcul du CA par produit
- l'export automatique de rapports CSV et Excel selon un planning défini

## Stack technique

`Kestra` `Python` `DuckDB` `Docker`

## Architecture du pipeline

![Diagramme de flux Kestra](https://github.com/user-attachments/assets/c95ee7c9-eae9-4816-9821-b353ecfa4751)

Le pipeline combine des tâches séquentielles et parallèles, avec trigger
temporel, logique de retry et remontée d'erreurs à chaque étape.

## Ce que j'ai construit

**Ingestion & conversion**
- Script Python de conversion des fichiers XLSX → CSV

**Nettoyage & transformation (DuckDB)**
- Requêtes SQL de nettoyage et dédoublonnage sur `web.csv`, `erp.csv`, `liaison.csv`
- Fusion des 3 tables via `INNER JOIN`

**Analyse & export**
- Calcul du CA par produit et CA total en SQL (DuckDB)
- Classification des vins par z-score (Python)
- Export du rapport de CA multi-feuilles (Python + openpyxl)

**Orchestration (Kestra)**
- Exécution séquentielle et parallèle des tâches
- Trigger temporel (scheduler)
- Retry automatique et remontée d'erreurs
- Tests de validation à chaque étape du flux

## Apprentissages clés

- Mise en place d'un pipeline de données robuste et automatisé de bout en bout
- Orchestration avec Kestra : gestion des dépendances entre tâches, parallélisme,
  gestion des erreurs
- Utilisation de DuckDB pour des transformations SQL légères et performantes
  directement sur fichiers
- Importance des tests intermédiaires pour éviter la propagation d'erreurs
  en production

## Lancer le projet

Prérequis : Docker installé
```bash
# Se placer dans le répertoire racine du projet
docker compose up -d
```

L'interface Kestra est ensuite accessible sur `http://localhost:8080`
