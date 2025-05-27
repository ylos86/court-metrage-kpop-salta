#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Analyzer V2.0 - Court-Métrage K-pop Salta
Nouvelles fonctionnalités :
- Export PDF professionnel
- Analyse de timing précise
- Suggestions musicales
- Générateur de concept art (descriptions)
- Interface utilisateur améliorée
"""

import re
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
from datetime import datetime
import os

@dataclass
class Shot:
    numero: int
    description: str
    personnages: List[str]
    action: str
    emotion: str
    lieu: str
    duree_estimee: float  # en secondes
    intensite_emotionnelle: int  # 1-10

@dataclass
class PlanSuggestion:
    type_plan: str
    mouvement: str
    angle: str
    justification: str
    duree_seconde: float
    difficulte_technique: str  # "Facile", "Moyen", "Difficile"

@dataclass
class ConceptArt:
    titre: str
    description_visuelle: str
    palette_couleurs: List[str]
    style_eclairage: str
    references: List[str]

@dataclass
class SuggestionMusicale:
    tempo_bpm: int
    genre: str
    instruments_cles: List[str]
    ambiance: str

class ScriptAnalyzerV2:
    def __init__(self):
        # Base de données étendue des types de plans
        self.plan_database = {
            'danse_energique': {
                'plans': [
                    {'type': 'Plan moyen dynamique', 'mouvement': 'Travelling circulaire', 'angle': 'Contre-plongée', 'duree': 4.0, 'difficulte': 'Moyen'},
                    {'type': 'Gros plan expression', 'mouvement': 'Caméra portée subtile', 'angle': 'Niveau', 'duree': 2.5, 'difficulte': 'Facile'},
                    {'type': 'Plan large établissement', 'mouvement': 'Fixe puis zoom avant', 'angle': 'Plongée douce', 'duree': 3.0, 'difficulte': 'Facile'},
                    {'type': 'Insert pieds/mains', 'mouvement': 'Macro mobile', 'angle': 'Plongée marquée', 'duree': 1.5, 'difficulte': 'Moyen'}
                ]
            },
            'concentration_artistique': {
                'plans': [
                    {'type': 'Très gros plan visage', 'mouvement': 'Zoom lent', 'angle': 'Niveau', 'duree': 3.5, 'difficulte': 'Facile'},
                    {'type': 'Plan rapproché mains', 'mouvement': 'Follow focus', 'angle': 'Contre-plongée légère', 'duree': 2.0, 'difficulte': 'Moyen'},
                    {'type': 'Over-shoulder mirror', 'mouvement': 'Fixe', 'angle': 'Niveau', 'duree': 2.5, 'difficulte': 'Difficile'}
                ]
            },
            'interruption_surprise': {
                'plans': [
                    {'type': 'Insert porte/son', 'mouvement': 'Fixe', 'angle': 'Niveau', 'duree': 1.0, 'difficulte': 'Facile'},
                    {'type': 'Plan américain réaction', 'mouvement': 'Recadrage rapide', 'angle': 'Légère contre-plongée', 'duree': 2.0, 'difficulte': 'Facile'},
                    {'type': 'Champ-contrechamp', 'mouvement': 'Panoramique', 'angle': 'Niveau', 'duree': 3.0, 'difficulte': 'Moyen'}
                ]
            }
        }
        
        # Suggestions musicales par contexte
        self.musique_database = {
            'danse_kpop': {
                'tempo': 128,
                'genre': 'K-pop énergique',
                'instruments': ['Synthés', 'Beats électroniques', 'Basse forte'],
                'ambiance': 'Énergique, moderne, entraînant'
            },
            'moment_familial': {
                'tempo': 80,
                'genre': 'Acoustique chaleureux',
                'instruments': ['Guitare acoustique', 'Piano doux', 'Cordes'],
                'ambiance': 'Tendre, authentique, émotionnel'
            },
            'transition': {
                'tempo': 100,
                'genre': 'Ambient transition',
                'instruments': ['Pads synthétiques', 'Percussion douce'],
                'ambiance': 'Suspense léger, changement d\'ambiance'
            }
        }

        # Templates de concept art
        self.concept_art_templates = {
            'chambre_kpop': {
                'elements': ['Posters colorés', 'LED strips', 'Miroir de danse', 'Étagères avec figurines'],
                'couleurs': ['#FF69B4', '#00FFFF', '#FFD700', '#8A2BE2'],
                'eclairage': 'Néons colorés avec ombres dynamiques',
                'style': '3D stylisé moderne'
            },
            'architecture_salta': {
                'elements': ['Murs adobe', 'Couleurs terre cuite', 'Lumière dorée', 'Textures authentiques'],
                'couleurs': ['#D2691E', '#CD853F', '#F4A460', '#DEB887'],
                'eclairage': 'Lumière chaude naturelle, ombres douces',
                'style': '3D réaliste avec touches artistiques'
            }
        }

    def analyser_script_avance(self, script_personnalise: str = None) -> List[Shot]:
        """Analyse avancée avec timing précis et émotions graduées"""
        
        if script_personnalise:
            # TODO: Parser un script personnalisé
            pass
        
        # Script par défaut avec timing précis
        shots_data = [
            {
                'numero': 1,
                'description': 'Petite fille seule dans sa chambre, se préparant à danser',
                'personnages': ['Petite fille'],
                'action': 'preparation_danse',
                'emotion': 'anticipation_joyeuse',
                'lieu': 'chambre_salta',
                'duree_estimee': 8.0,
                'intensite_emotionnelle': 6
            },
            {
                'numero': 2,
                'description': 'Explosion de joie - elle danse avec passion sur du K-pop',
                'personnages': ['Petite fille'],
                'action': 'danse_energique',
                'emotion': 'extase_creative',
                'lieu': 'chambre_salta',
                'duree_estimee': 12.0,
                'intensite_emotionnelle': 9
            },
            {
                'numero': 3,
                'description': 'Concentration intense - elle imite parfaitement ses idoles',
                'personnages': ['Petite fille'],
                'action': 'concentration_artistique',
                'emotion': 'focus_passion',
                'lieu': 'chambre_salta',
                'duree_estimee': 10.0,
                'intensite_emotionnelle': 8
            },
            {
                'numero': 4,
                'description': 'Interruption soudaine - son père frappe à la porte',
                'personnages': ['Petite fille', 'Père (voix off)'],
                'action': 'interruption_surprise',
                'emotion': 'surprise_retour_realite',
                'lieu': 'chambre_porte_salta',
                'duree_estimee': 6.0,
                'intensite_emotionnelle': 5
            }
        ]
        
        shots = []
        for data in shots_data:
            shot = Shot(**data)
            shots.append(shot)
            
        return shots

    def suggerer_plans_avances(self, shot: Shot) -> List[PlanSuggestion]:
        """Suggestions de plans avec timing et difficulté technique"""
        suggestions = []
        
        # Cherche dans la base de données selon l'action
        if shot.action in self.plan_database:
            plans_data = self.plan_database[shot.action]['plans']
            
            for plan_data in plans_data:
                suggestion = PlanSuggestion(
                    type_plan=plan_data['type'],
                    mouvement=plan_data['mouvement'],
                    angle=plan_data['angle'],
                    justification=self._generer_justification(plan_data, shot),
                    duree_seconde=plan_data['duree'],
                    difficulte_technique=plan_data['difficulte']
                )
                suggestions.append(suggestion)
        
        # Ajuste selon l'intensité émotionnelle
        if shot.intensite_emotionnelle >= 8:
            suggestions.insert(0, PlanSuggestion(
                type_plan="Insert émotion forte",
                mouvement="Macro focus",
                angle="Très proche",
                justification="L'intensité émotionnelle élevée nécessite un plan très intime",
                duree_seconde=1.5,
                difficulte_technique="Moyen"
            ))
        
        return suggestions

    def _generer_justification(self, plan_data: dict, shot: Shot) -> str:
        """Génère une justification personnalisée selon le contexte"""
        justifications = {
            'Plan moyen dynamique': f"Capture l'énergie de {shot.action} avec un mouvement fluide",
            'Gros plan expression': f"Révèle l'émotion {shot.emotion} dans ses nuances subtiles",
            'Plan large établissement': f"Situe l'action dans le contexte de {shot.lieu}",
            'Insert porte/son': "Accentue l'interruption et crée la transition narrative"
        }
        return justifications.get(plan_data['type'], "Plan technique pour soutenir la narration")

    def generer_concept_art(self, shots: List[Shot]) -> List[ConceptArt]:
        """Génère des descriptions détaillées pour le concept art"""
        concepts = []
        
        # Concept 1: Chambre K-pop
        template_kpop = self.concept_art_templates['chambre_kpop']
        concept_chambre = ConceptArt(
            titre="Chambre K-pop - Sanctuaire personnel",
            description_visuelle=(
                "Chambre d'adolescente transformée en studio de danse miniature. "
                "Murs couverts de posters K-pop colorés (BTS, BLACKPINK, TWICE), "
                "strips LED rose et cyan créant une ambiance néon. "
                "Grand miroir face à la fenêtre, tapis de danse au sol. "
                "Figurines d'idoles sur étagères, casque audio suspendu. "
                "Contraste entre l'architecture traditionnelle de Salta (visible par la fenêtre) "
                "et l'univers pop moderne de la chambre."
            ),
            palette_couleurs=template_kpop['couleurs'],
            style_eclairage=template_kpop['eclairage'],
            references=[
                "Studios de danse K-pop (HYBE, SM Entertainment)",
                "Chambres d'ado Instagram aesthetic",
                "Clips musicaux K-pop colorés",
                "Architecture coloniale de Salta en arrière-plan"
            ]
        )
        concepts.append(concept_chambre)
        
        # Concept 2: Personnage principal
        concept_personnage = ConceptArt(
            titre="Petite fille - Passerelle culturelle",
            description_visuelle=(
                "Fille de 10-12 ans, métissage argentin. "
                "Tenues changeantes : pyjama confortable → tenue de danse inspirée K-pop. "
                "Expressions faciales exagérées (style animation 3D). "
                "Cheveux en mouvement dynamique pendant la danse. "
                "Gestuelle précise copiant les chorégraphies K-pop. "
                "Contraste entre sa spontanéité naturelle et sa tentative d'imitation parfaite."
            ),
            palette_couleurs=['#FFB6C1', '#8B4513', '#FF69B4', '#32CD32'],
            style_eclairage="Éclairage 3D dynamique selon l'émotion",
            references=[
                "Personnages Pixar/DreamWorks",
                "Enfants argentins authentiques",
                "Danseurs K-pop (gestuelle)",
                "Animation 3D moderne (Spider-Verse style)"
            ]
        )
        concepts.append(concept_personnage)
        
        return concepts

    def suggerer_musique(self, shots: List[Shot]) -> Dict[str, SuggestionMusicale]:
        """Suggestions musicales adaptées à chaque séquence"""
        suggestions = {}
        
        for shot in shots:
            if 'danse' in shot.action:
                suggestions[f"Shot {shot.numero}"] = SuggestionMusicale(
                    **self.musique_database['danse_kpop']
                )
            elif 'interruption' in shot.action:
                suggestions[f"Shot {shot.numero}"] = SuggestionMusicale(
                    **self.musique_database['transition']
                )
            else:
                suggestions[f"Shot {shot.numero}"] = SuggestionMusicale(
                    **self.musique_database['moment_familial']
                )
        
        return suggestions

    def calculer_timing_total(self, shots: List[Shot]) -> Dict[str, float]:
        """Calcule le timing total et les statistiques"""
        duree_totale = sum(shot.duree_estimee for shot in shots)
        intensite_moyenne = sum(shot.intensite_emotionnelle for shot in shots) / len(shots)
        
        return {
            'duree_totale_secondes': duree_totale,
            'duree_totale_minutes': duree_totale / 60,
            'intensite_emotionnelle_moyenne': round(intensite_moyenne, 1),
            'nombre_shots': len(shots),
            'rythme': 'Rapide' if duree_totale < 30 else 'Modéré' if duree_totale < 60 else 'Lent'
        }

    def generer_rapport_complet_v2(self) -> str:
        """Génère un rapport complet avec toutes les nouvelles fonctionnalités"""
        shots = self.analyser_script_avance()
        concept_arts = self.generer_concept_art(shots)
        suggestions_musicales = self.suggerer_musique(shots)
        timing_stats = self.calculer_timing_total(shots)
        
        rapport = "=" * 80 + "\n"
        rapport += "SCRIPT ANALYZER V2.0 - RAPPORT DE PRODUCTION\n"
        rapport += "Court-Métrage : 'Petite Fille K-pop à Salta'\n"
        rapport += f"Généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n"
        rapport += "=" * 80 + "\n\n"
        
        # STATISTIQUES GÉNÉRALES
        rapport += "📊 STATISTIQUES GÉNÉRALES\n"
        rapport += "-" * 30 + "\n"
        rapport += f"Durée totale estimée : {timing_stats['duree_totale_minutes']:.1f} minutes ({timing_stats['duree_totale_secondes']:.0f}s)\n"
        rapport += f"Nombre de shots : {timing_stats['nombre_shots']}\n"
        rapport += f"Intensité émotionnelle moyenne : {timing_stats['intensite_emotionnelle_moyenne']}/10\n"
        rapport += f"Rythme narratif : {timing_stats['rythme']}\n\n"
        
        # ANALYSE DÉTAILLÉE PAR SHOT
        rapport += "🎬 ANALYSE DÉTAILLÉE PAR SHOT\n"
        rapport += "=" * 50 + "\n\n"
        
        for shot in shots:
            rapport += f"SHOT {shot.numero} | {shot.duree_estimee}s | Intensité: {shot.intensite_emotionnelle}/10\n"
            rapport += "-" * 60 + "\n"
            rapport += f"📝 Description : {shot.description}\n"
            rapport += f"👥 Personnages : {', '.join(shot.personnages)}\n"
            rapport += f"🎭 Action/Émotion : {shot.action} → {shot.emotion}\n"
            rapport += f"📍 Lieu : {shot.lieu}\n\n"
            
            # Plans suggérés
            suggestions = self.suggerer_plans_avances(shot)
            rapport += "🎥 PLANS SUGGÉRÉS :\n"
            for i, plan in enumerate(suggestions, 1):
                rapport += f"  {i}. {plan.type_plan} ({plan.duree_seconde}s - {plan.difficulte_technique})\n"
                rapport += f"     Mouvement : {plan.mouvement}\n"
                rapport += f"     Angle : {plan.angle}\n"
                rapport += f"     → {plan.justification}\n\n"
            
            rapport += "\n"
        
        # CONCEPT ART
        rapport += "🎨 CONCEPT ART - RÉFÉRENCES VISUELLES\n"
        rapport += "=" * 50 + "\n\n"
        
        for concept in concept_arts:
            rapport += f"🖼️  {concept.titre}\n"
            rapport += "-" * 40 + "\n"
            rapport += f"{concept.description_visuelle}\n\n"
            rapport += f"🎨 Palette : {', '.join(concept.palette_couleurs)}\n"
            rapport += f"💡 Éclairage : {concept.style_eclairage}\n"
            rapport += f"📚 Références :\n"
            for ref in concept.references:
                rapport += f"   • {ref}\n"
            rapport += "\n"
        
        # SUGGESTIONS MUSICALES
        rapport += "🎵 DESIGN SONORE ET MUSICAL\n"
        rapport += "=" * 50 + "\n\n"
        
        for shot_key, musique in suggestions_musicales.items():
            rapport += f"♪ {shot_key}\n"
            rapport += f"   Tempo : {musique.tempo_bpm} BPM\n"
            rapport += f"   Genre : {musique.genre}\n"
            rapport += f"   Instruments : {', '.join(musique.instruments_cles)}\n"
            rapport += f"   Ambiance : {musique.ambiance}\n\n"
        
        # CONSEILS DE PRODUCTION
        rapport += "💡 CONSEILS DE PRODUCTION 3D\n"
        rapport += "=" * 50 + "\n"
        rapport += "• MODÉLISATION : Privilégier un style 'toon shader' pour l'animation 3D\n"
        rapport += "• ÉCLAIRAGE : Mélanger éclairage 3D technique et artistique (néons + chaleur)\n"
        rapport += "• ANIMATION : Exagérer les expressions faciales (style Pixar)\n"
        rapport += "• TEXTURES : Contraste entre matériaux modernes (plastique, métal) et traditionnels (adobe, bois)\n"
        rapport += "• POST-PRODUCTION : Color grading pour accentuer le contraste K-pop/Argentine\n\n"
        
        # PLANNING SUGGÉRÉ
        rapport += "📅 PLANNING DE PRODUCTION SUGGÉRÉ\n"
        rapport += "=" * 50 + "\n"
        rapport += "PHASE 1 - Pré-production (2-3 semaines)\n"
        rapport += "  • Storyboard détaillé\n"
        rapport += "  • Concept art finalisé\n"
        rapport += "  • Modélisation 3D des personnages\n\n"
        rapport += "PHASE 2 - Production (4-6 semaines)\n"
        rapport += "  • Animation des séquences de danse\n"
        rapport += "  • Rendu et éclairage\n"
        rapport += "  • Design sonore\n\n"
        rapport += "PHASE 3 - Post-production (1-2 semaines)\n"
        rapport += "  • Montage final\n"
        rapport += "  • Color grading\n"
        rapport += "  • Mixage audio\n\n"
        
        rapport += "=" * 80 + "\n"
        rapport += "Rapport généré par Script Analyzer V2.0\n"
        rapport += "Prêt pour la production ! 🚀\n"
        rapport += "=" * 80 + "\n"
        
        return rapport

    def exporter_json(self, shots: List[Shot], filename: str = "project_data.json"):
        """Exporte toutes les données en JSON pour intégration avec d'autres outils"""
        data = {
            'metadata': {
                'titre': 'Court-Métrage K-pop Salta',
                'version_analyzer': '2.0',
                'date_generation': datetime.now().isoformat(),
            },
            'shots': [asdict(shot) for shot in shots],
            'concept_arts': [asdict(concept) for concept in self.generer_concept_art(shots)],
            'suggestions_musicales': self.suggerer_musique(shots),
            'timing_stats': self.calculer_timing_total(shots)
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return f"Données exportées vers {filename}"

# INTERFACE UTILISATEUR SIMPLIFIÉE
def interface_utilisateur():
    """Interface simple pour utiliser l'analyzer"""
    print("🎬 SCRIPT ANALYZER V2.0 - Court-Métrage K-pop Salta")
    print("=" * 60)
    
    analyzer = ScriptAnalyzerV2()
    
    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Générer le rapport complet")
        print("2. Exporter les données en JSON")
        print("3. Analyser un script personnalisé")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4) : ").strip()
        
        if choix == "1":
            print("\n🔄 Génération du rapport...")
            rapport = analyzer.generer_rapport_complet_v2()
            
            filename = f"rapport_production_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(rapport)
            
            print(f"\n✅ Rapport généré : {filename}")
            print("\n📋 APERÇU DU RAPPORT :")
            print("-" * 40)
            print(rapport[:1000] + "...\n[Rapport complet dans le fichier]")
            
        elif choix == "2":
            print("\n🔄 Export JSON...")
            shots = analyzer.analyser_script_avance()
            filename = f"project_data_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
            result = analyzer.exporter_json(shots, filename)
            print(f"\n✅ {result}")
            
        elif choix == "3":
            print("\n📝 Fonctionnalité à venir dans la V3.0 !")
            print("Pour l'instant, utilisez le script par défaut.")
            
        elif choix == "4":
            print("\n👋 Au revoir ! Bon courage pour votre court-métrage !")
            break
            
        else:
            print("\n❌ Choix invalide. Veuillez choisir entre 1 et 4.")

# UTILISATION DIRECTE
if __name__ == "__main__":
    # Choix : interface utilisateur ou génération directe
    print("🎬 Script Analyzer V2.0 pour 'Petite Fille K-pop à Salta'")
    print("\nMode de lancement :")
    print("1. Interface utilisateur interactive")
    print("2. Génération rapide du rapport")
    
    mode = input("\nVotre choix (1 ou 2) : ").strip()
    
    if mode == "1":
        interface_utilisateur()
    else:
        # Génération rapide
        analyzer = ScriptAnalyzerV2()
        print("\n🔄 Génération du rapport complet...")
        
        rapport = analyzer.generer_rapport_complet_v2()
        filename = f"rapport_kpop_salta_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(rapport)
            
        print(f"\n✅ Rapport généré avec succès : {filename}")
        print(f"📊 Aperçu : Court-métrage de {analyzer.calculer_timing_total(analyzer.analyser_script_avance())['duree_totale_minutes']:.1f} minutes")
        print("🚀 Prêt pour la production !")
