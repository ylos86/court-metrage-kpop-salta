#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyseur de Script pour Court-Métrage
Génère des suggestions de plans de caméra et mood board
"""

import re
from dataclasses import dataclass
from typing import List, Dict
import json

@dataclass
class Shot:
    """Représente un plan avec ses caractéristiques"""
    numero: int
    description: str
    personnages: List[str]
    action: str
    emotion: str
    lieu: str

@dataclass
class PlanSuggestion:
    """Suggestion de plan de caméra"""
    type_plan: str
    mouvement: str
    angle: str
    justification: str

@dataclass
class MoodElement:
    """Élément du mood board"""
    palette_couleurs: List[str]
    style_eclairage: str
    ambiance: str
    references_visuelles: List[str]

class ScriptAnalyzer:
    def __init__(self):
        # Base de données des types de plans selon le contexte
        self.plan_suggestions = {
            'danse': {
                'types': ['Plan moyen', 'Plan américain', 'Gros plan pieds', 'Plan large'],
                'mouvements': ['Travelling circulaire', 'Caméra portée', 'Steadicam'],
                'angles': ['Contre-plongée dynamique', 'Plongée légère', 'Niveau']
            },
            'emotion_forte': {
                'types': ['Gros plan', 'Très gros plan', 'Plan rapproché'],
                'mouvements': ['Fixe', 'Zoom lent', 'Recadrage subtil'],
                'angles': ['Niveau', 'Légère plongée']
            },
            'interaction': {
                'types': ['Plan moyen', 'Champ-contrechamp', 'Plan américain'],
                'mouvements': ['Panoramique', 'Travelling avant', 'Fixe'],
                'angles': ['Niveau', 'Contre-plongée sur enfant']
            }
        }
        
        # Styles visuels pour l'animation 3D
        self.mood_database = {
            'kpop_chambre': {
                'couleurs': ['#FF69B4', '#00FFFF', '#FFD700', '#FF1493', '#8A2BE2'],
                'eclairage': 'Éclairage néon coloré, LED strips, lumière dynamique',
                'ambiance': 'Énergique, pop, moderne, urbaine',
                'references': ['Studios de danse K-pop', 'Clips musicaux colorés', 'Chambres d\'ado Instagram']
            },
            'argentine_salta': {
                'couleurs': ['#D2691E', '#CD853F', '#F4A460', '#DEB887', '#BC8F8F'],
                'eclairage': 'Lumière dorée, ombres chaudes, contraste marqué',
                'ambiance': 'Chaleureux, authentique, familial',
                'references': ['Architecture coloniale', 'Couleurs terre cuite', 'Lumière d\'Amérique du Sud']
            },
            'animation_3d_graphique': {
                'couleurs': ['Palettes saturées', 'Contrastes forts', 'Couleurs pures'],
                'eclairage': 'Éclairage 3D dramatique, jeu d\'ombres graphiques',
                'ambiance': 'Stylisé, moderne, cinématographique',
                'references': ['Pixar stylisé', 'Spider-Verse', 'Animation 3D moderne']
            }
        }

    def analyser_script(self, script_text: str) -> List[Shot]:
        """Analyse le script et extrait les informations de chaque shot"""
        shots = []
        
        # Pour ce prototype, on définit manuellement les 3 shots
        shots_data = [
            {
                'numero': 1,
                'description': 'Petite fille dans sa chambre, dansant sur de la K-pop',
                'personnages': ['Petite fille'],
                'action': 'danse',
                'emotion': 'joie_energie',
                'lieu': 'chambre_salta'
            },
            {
                'numero': 2,
                'description': 'Elle imite ses stars K-pop avec passion',
                'personnages': ['Petite fille'],
                'action': 'danse_imitation',
                'emotion': 'concentration_passion',
                'lieu': 'chambre_salta'
            },
            {
                'numero': 3,
                'description': 'Le père frappe à la porte pour qu\'elle vienne l\'aider',
                'personnages': ['Petite fille', 'Père'],
                'action': 'interaction',
                'emotion': 'interruption_surprise',
                'lieu': 'chambre_porte'
            }
        ]
        
        for data in shots_data:
            shot = Shot(**data)
            shots.append(shot)
            
        return shots

    def suggerer_plans(self, shot: Shot) -> List[PlanSuggestion]:
        """Génère des suggestions de plans pour un shot donné"""
        suggestions = []
        
        if 'danse' in shot.action:
            # Plans dynamiques pour la danse
            suggestions.extend([
                PlanSuggestion(
                    type_plan="Plan moyen dynamique",
                    mouvement="Travelling circulaire",
                    angle="Contre-plongée légère",
                    justification="Capture l'énergie de la danse et valorise le personnage"
                ),
                PlanSuggestion(
                    type_plan="Gros plan visage",
                    mouvement="Caméra portée subtile",
                    angle="Niveau",
                    justification="Montre l'expression de concentration et de joie"
                ),
                PlanSuggestion(
                    type_plan="Plan large",
                    mouvement="Fixe puis zoom",
                    angle="Plongée douce",
                    justification="Établit l'espace de la chambre et le contexte"
                )
            ])
            
        if 'interaction' in shot.action:
            suggestions.extend([
                PlanSuggestion(
                    type_plan="Plan américain",
                    mouvement="Panoramique porte → fille",
                    angle="Niveau",
                    justification="Transition naturelle entre les deux personnages"
                ),
                PlanSuggestion(
                    type_plan="Insert porte",
                    mouvement="Fixe",
                    angle="Niveau",
                    justification="Accentue l'interruption sonore"
                )
            ])
            
        return suggestions

    def generer_mood_board(self, shots: List[Shot]) -> Dict:
        """Génère des éléments de mood board basés sur les shots"""
        mood_elements = {
            'palette_principale': [],
            'styles_eclairage': [],
            'ambiances': [],
            'references_visuelles': []
        }
        
        # Combine les éléments K-pop, Argentine et animation 3D
        kpop_mood = self.mood_database['kpop_chambre']
        argentine_mood = self.mood_database['argentine_salta']
        anim_mood = self.mood_database['animation_3d_graphique']
        
        mood_elements['palette_principale'] = kpop_mood['couleurs'] + argentine_mood['couleurs'][:3]
        mood_elements['styles_eclairage'] = [
            kpop_mood['eclairage'],
            argentine_mood['eclairage'],
            anim_mood['eclairage']
        ]
        mood_elements['ambiances'] = [
            "Contraste culturel : K-pop moderne vs tradition argentine",
            "Énergie juvénile dans cadre familial chaleureux",
            "Style 3D graphique avec personnalité"
        ]
        mood_elements['references_visuelles'] = [
            "Chambre d'ado avec posters K-pop colorés",
            "Architecture de Salta en arrière-plan",
            "Style d'animation Pixar/DreamWorks moderne",
            "Éclairage néon rose/bleu contrastant avec tons chauds",
            "Expressions faciales exagérées (style animation 3D)"
        ]
        
        return mood_elements

    def generer_rapport_complet(self, script_text: str) -> str:
        """Génère un rapport complet d'analyse"""
        shots = self.analyser_script(script_text)
        mood_board = self.generer_mood_board(shots)
        
        rapport = "="*60 + "\n"
        rapport += "ANALYSE DE SCRIPT - COURT-MÉTRAGE\n"
        rapport += "Projet : Petite fille K-pop à Salta\n"
        rapport += "="*60 + "\n\n"
        
        # Analyse par shot
        for shot in shots:
            rapport += f"SHOT {shot.numero}\n"
            rapport += "-" * 20 + "\n"
            rapport += f"Description : {shot.description}\n"
            rapport += f"Personnages : {', '.join(shot.personnages)}\n"
            rapport += f"Action : {shot.action}\n"
            rapport += f"Émotion : {shot.emotion}\n\n"
            
            # Suggestions de plans
            suggestions = self.suggerer_plans(shot)
            rapport += "SUGGESTIONS DE PLANS :\n"
            for i, suggestion in enumerate(suggestions, 1):
                rapport += f"{i}. {suggestion.type_plan}\n"
                rapport += f"   Mouvement : {suggestion.mouvement}\n"
                rapport += f"   Angle : {suggestion.angle}\n"
                rapport += f"   Pourquoi : {suggestion.justification}\n\n"
            
            rapport += "\n"
        
        # Mood board
        rapport += "MOOD BOARD - STYLE VISUEL\n"
        rapport += "="*30 + "\n"
        rapport += f"Palette couleurs : {', '.join(mood_board['palette_principale'][:6])}\n\n"
        
        rapport += "STYLES D'ÉCLAIRAGE :\n"
        for style in mood_board['styles_eclairage']:
            rapport += f"• {style}\n"
        
        rapport += "\nAMBIANCES CLÉS :\n"
        for ambiance in mood_board['ambiances']:
            rapport += f"• {ambiance}\n"
            
        rapport += "\nRÉFÉRENCES VISUELLES :\n"
        for ref in mood_board['references_visuelles']:
            rapport += f"• {ref}\n"
        
        return rapport

# Utilisation du script
if __name__ == "__main__":
    analyzer = ScriptAnalyzer()
    
    # Script d'exemple (vos 3 shots)
    script_exemple = """
    SHOT 1: Petite fille dans sa chambre, dansant sur de la K-pop
    SHOT 2: Elle imite ses stars K-pop avec passion  
    SHOT 3: Le père frappe à la porte pour qu'elle vienne l'aider
    """
    
    # Génération du rapport
    rapport = analyzer.generer_rapport_complet(script_exemple)
    print(rapport)
    
    # Sauvegarde en fichier
    with open("analyse_script_kpop_salta.txt", "w", encoding="utf-8") as f:
        f.write(rapport)
    
    print("\n" + "="*60)
    print("Rapport sauvegardé dans 'analyse_script_kpop_salta.txt'")
    print("="*60)
