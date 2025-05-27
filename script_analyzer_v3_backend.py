#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Analyzer V3.0 - Backend Complet
Court-Métrage K-pop Salta
Toutes les fonctionnalités avancées : IA, PDF, 3D, Sync Musical
"""

import json
import os
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
import base64
from pathlib import Path
import subprocess
import tempfile

# Tentative d'imports optionnels
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

@dataclass
class AIImagePrompt:
    """Prompt optimisé pour génération d'images IA"""
    titre: str
    prompt_detaille: str
    style_artistique: str
    parametres_techniques: Dict[str, Any]
    references_visuelles: List[str]

@dataclass
class ExportConfig:
    """Configuration pour les exports"""
    include_shots: bool = True
    include_concept_art: bool = True
    include_storyboard: bool = True
    include_music: bool = True
    include_planning: bool = True
    include_budget: bool = True
    format_export: str = "pdf"  # pdf, html, json, xml

@dataclass
class BlenderScript:
    """Script Blender généré automatiquement"""
    nom_script: str
    code_python: str
    description: str
    compatibilite: str

@dataclass
class BudgetEstimate:
    """Estimation budgétaire automatique"""
    pre_production: float
    production: float
    post_production: float
    materiel: float
    logiciels: float
    total: float

class ScriptAnalyzerV3:
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.config = self._load_config()
        self.ai_prompts = []
        self.blender_scripts = []
        
        # Initialisation des dossiers de projet
        self._init_project_structure()
        
    def _load_config(self) -> Dict:
        """Charge la configuration du projet"""
        config_file = self.project_path / "config.json"
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Configuration par défaut
        return {
            "project_name": "Court-Métrage K-pop Salta",
            "version": "3.0",
            "ai_service": "local",  # local, openai, midjourney
            "export_quality": "high",
            "blender_version": "3.6",
            "target_resolution": "4K"
        }
    
    def _init_project_structure(self):
        """Initialise la structure de dossiers du projet"""
        folders = [
            "exports", "ai_generated", "blender_scripts", 
            "storyboard", "music_sync", "pdf_reports", "concept_art"
        ]
        
        for folder in folders:
            (self.project_path / folder).mkdir(exist_ok=True)

    def generate_ai_image_prompts(self) -> List[AIImagePrompt]:
        """Génère des prompts optimisés pour l'IA"""
        prompts = []
        
        # Prompt 1: Chambre K-pop
        prompt_chambre = AIImagePrompt(
            titre="Chambre K-pop Sanctuaire",
            prompt_detaille=(
                "3D rendered teenage bedroom transformed into K-pop dance studio, "
                "vibrant LED strip lights in pink and cyan, colorful K-pop posters "
                "(BTS, BLACKPINK, TWICE), large dance mirror, wooden floor with dance mat, "
                "Argentina Salta colonial architecture visible through window, "
                "warm golden sunlight contrasting with neon interior lights, "
                "Pixar-style 3D animation aesthetic, highly detailed textures, "
                "cinematic lighting setup, 4K quality, stylized realism"
            ),
            style_artistique="3D Animation, Pixar-style, Modern K-pop Aesthetic",
            parametres_techniques={
                "aspect_ratio": "16:9",
                "resolution": "3840x2160",
                "lighting": "Mixed (neon + natural)",
                "render_engine": "Cycles/Eevee compatible"
            },
            references_visuelles=[
                "HYBE Corporation dance studios",
                "Modern teenage bedrooms",
                "Salta colonial architecture",
                "K-pop music video sets"
            ]
        )
        prompts.append(prompt_chambre)
        
        # Prompt 2: Personnage Principal
        prompt_personnage = AIImagePrompt(
            titre="Petite Fille Argentine K-pop Fan",
            prompt_detaille=(
                "3D animated character design, 10-12 years old Argentine girl, "
                "mixed ethnicity features, expressive large eyes, dynamic K-pop inspired outfit, "
                "hair in motion from dancing, exaggerated facial expressions, "
                "Pixar/DreamWorks animation style, vibrant colors, "
                "multiple poses showing dance movements, character turnaround sheet, "
                "high-quality 3D model reference, stylized but authentic, "
                "suitable for 3D animation production"
            ),
            style_artistique="Character Design, 3D Animation, Pixar-inspired",
            parametres_techniques={
                "model_type": "3D Character Reference",
                "polygon_count": "Medium (animation-ready)",
                "rigging_ready": True,
                "facial_animation": "Advanced expressions"
            },
            references_visuelles=[
                "Pixar character designs",
                "Argentine children photography",
                "K-pop dancer poses",
                "Animation character sheets"
            ]
        )
        prompts.append(prompt_personnage)
        
        # Prompt 3: Storyboard Cinématique
        prompt_storyboard = AIImagePrompt(
            titre="Storyboard Séquence Danse",
            prompt_detaille=(
                "Professional storyboard panels, cinematic shot composition, "
                "4 sequential panels showing dance sequence progression, "
                "camera angles marked, movement arrows, lighting notes, "
                "3D animation pre-visualization style, clean line art, "
                "professional film production quality, shot types labeled, "
                "timing annotations, emotional beats marked"
            ),
            style_artistique="Storyboard, Pre-visualization, Professional Film",
            parametres_techniques={
                "format": "Sequential panels",
                "annotation_style": "Professional film",
                "shot_types": "Marked and labeled",
                "aspect_ratio": "Cinemascope compatible"
            },
            references_visuelles=[
                "Pixar storyboard examples",
                "Professional film storyboards",
                "Animation pre-vis",
                "K-pop music video storyboards"
            ]
        )
        prompts.append(prompt_storyboard)
        
        self.ai_prompts = prompts
        return prompts

    def generate_blender_scripts(self) -> List[BlenderScript]:
        """Génère des scripts Blender automatiques"""
        scripts = []
        
        # Script 1: Setup de caméra automatique
        camera_script = BlenderScript(
            nom_script="camera_movements_kpop.py",
            code_python="""
import bpy
import mathutils
from mathutils import Vector
import bmesh

def setup_kpop_cameras():
    \"\"\"Configure les caméras pour les séquences K-pop\"\"\"
    
    # Supprimer caméras existantes
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA':
            obj.select_set(True)
    bpy.ops.object.delete()
    
    # Shot 1: Plan large établissement
    bpy.ops.object.camera_add(location=(5, -8, 3))
    cam1 = bpy.context.active_object
    cam1.name = "Camera_Shot01_Wide"
    cam1.rotation_euler = (1.1, 0, 0.8)
    
    # Keyframes pour zoom avant
    cam1.keyframe_insert(data_path="location", frame=1)
    cam1.location = (3, -5, 2.5)
    cam1.keyframe_insert(data_path="location", frame=120)
    
    # Shot 2: Travelling circulaire dynamique
    bpy.ops.object.camera_add(location=(4, -4, 2))
    cam2 = bpy.context.active_object
    cam2.name = "Camera_Shot02_Circular"
    
    # Animation circulaire
    for frame in range(1, 180):
        angle = (frame / 180) * 6.28  # 2 tours
        x = 4 * mathutils.cos(angle)
        y = 4 * mathutils.sin(angle) - 4
        z = 2 + mathutils.sin(angle * 2) * 0.5
        
        cam2.location = (x, y, z)
        cam2.keyframe_insert(data_path="location", frame=frame)
        
        # Rotation pour garder le sujet en cadre
        cam2.rotation_euler = (1.2, 0, angle + 1.57)
        cam2.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    # Shot 3: Gros plan avec focus pull
    bpy.ops.object.camera_add(location=(1, -2, 1.6))
    cam3 = bpy.context.active_object
    cam3.name = "Camera_Shot03_Closeup"
    cam3.rotation_euler = (1.3, 0, 0.2)
    
    # Configuration depth of field
    cam3.data.dof.use_dof = True
    cam3.data.dof.focus_distance = 2.0
    cam3.data.dof.aperture_fstop = 1.4
    
    # Shot 4: Plan américain réaction
    bpy.ops.object.camera_add(location=(2, -3, 1.8))
    cam4 = bpy.context.active_object
    cam4.name = "Camera_Shot04_American"
    cam4.rotation_euler = (1.15, 0, 0.3)
    
    print("Caméras K-pop configurées avec succès!")

def setup_lighting_kpop():
    \"\"\"Configure l'éclairage K-pop avec néons\"\"\"
    
    # Supprimer éclairage existant
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type == 'LIGHT':
            obj.select_set(True)
    bpy.ops.object.delete()
    
    # Éclairage principal - LED strips roses
    bpy.ops.object.light_add(type='AREA', location=(0, 2, 3))
    light1 = bpy.context.active_object
    light1.name = "LED_Strip_Pink"
    light1.data.energy = 50
    light1.data.color = (1.0, 0.4, 0.7)  # Rose K-pop
    light1.data.size = 2
    light1.data.size_y = 0.1
    
    # LED strips cyan
    bpy.ops.object.light_add(type='AREA', location=(3, 0, 3))
    light2 = bpy.context.active_object
    light2.name = "LED_Strip_Cyan"
    light2.data.energy = 45
    light2.data.color = (0.0, 1.0, 1.0)  # Cyan
    light2.data.size = 2
    light2.data.size_y = 0.1
    
    # Lumière dorée Argentine (fenêtre)
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 8))
    sun_light = bpy.context.active_object
    sun_light.name = "Salta_Golden_Light"
    sun_light.data.energy = 3
    sun_light.data.color = (1.0, 0.8, 0.6)  # Doré chaud
    sun_light.rotation_euler = (0.5, 0.3, -0.8)
    
    # Éclairage de remplissage
    bpy.ops.object.light_add(type='AREA', location=(-2, -2, 2))
    fill_light = bpy.context.active_object
    fill_light.name = "Fill_Soft"
    fill_light.data.energy = 20
    fill_light.data.color = (0.9, 0.9, 1.0)  # Bleu doux
    
    print("Éclairage K-pop configuré!")

# Exécution
if __name__ == "__main__":
    setup_kpop_cameras()
    setup_lighting_kpop()
    print("Setup Blender K-pop terminé!")
""",
            description="Script automatique pour configurer caméras et éclairage K-pop dans Blender",
            compatibilite="Blender 3.0+"
        )
        scripts.append(camera_script)
        
        # Script 2: Animation et rigging
        animation_script = BlenderScript(
            nom_script="character_animation_kpop.py",
            code_python="""
import bpy
import mathutils

def create_kpop_dance_animation():
    \"\"\"Crée une animation de base pour la danse K-pop\"\"\"
    
    # Vérifier qu'un personnage est sélectionné
    if not bpy.context.active_object or bpy.context.active_object.type != 'ARMATURE':
        print("Erreur: Sélectionnez un armature de personnage")
        return
    
    armature = bpy.context.active_object
    
    # Poses clés K-pop
    kpop_poses = [
        {"frame": 1, "pose": "idle", "energy": 0.3},
        {"frame": 30, "pose": "preparation", "energy": 0.6},
        {"frame": 60, "pose": "explosion_joie", "energy": 1.0},
        {"frame": 120, "pose": "concentration", "energy": 0.8},
        {"frame": 150, "pose": "finale", "energy": 0.9}
    ]
    
    # Configuration des keyframes
    bpy.context.scene.frame_set(1)
    
    for pose_data in kpop_poses:
        frame = pose_data["frame"]
        energy = pose_data["energy"]
        
        bpy.context.scene.frame_set(frame)
        
        # Animation des bras (simulation gestuelle K-pop)
        if "arm_L" in armature.pose.bones:
            bone_L = armature.pose.bones["arm_L"]
            bone_L.rotation_quaternion = mathutils.Quaternion((1, energy, 0.5, 0.2))
            bone_L.keyframe_insert(data_path="rotation_quaternion")
        
        if "arm_R" in armature.pose.bones:
            bone_R = armature.pose.bones["arm_R"]
            bone_R.rotation_quaternion = mathutils.Quaternion((1, -energy, 0.5, -0.2))
            bone_R.keyframe_insert(data_path="rotation_quaternion")
        
        # Animation du torse
        if "spine" in armature.pose.bones:
            spine = armature.pose.bones["spine"]
            spine.rotation_euler = (0, 0, energy * 0.1)
            spine.keyframe_insert(data_path="rotation_euler")
    
    print(f"Animation K-pop créée avec {len(kpop_poses)} poses clés!")

def setup_facial_expressions():
    \"\"\"Configure les expressions faciales exagérées\"\"\"
    
    obj = bpy.context.active_object
    if not obj or not obj.data.shape_keys:
        print("Erreur: Objet avec shape keys requis")
        return
    
    # Expressions clés
    expressions = [
        {"frame": 30, "joy": 0.8, "surprise": 0.2},
        {"frame": 60, "joy": 1.0, "energy": 1.0},
        {"frame": 120, "concentration": 0.9, "focus": 0.8}
    ]
    
    for expr in expressions:
        frame = expr["frame"]
        bpy.context.scene.frame_set(frame)
        
        for shape_name, value in expr.items():
            if shape_name != "frame" and shape_name in obj.data.shape_keys.key_blocks:
                obj.data.shape_keys.key_blocks[shape_name].value = value
                obj.data.shape_keys.key_blocks[shape_name].keyframe_insert(data_path="value")
    
    print("Expressions faciales configurées!")

# Exécution
if __name__ == "__main__":
    create_kpop_dance_animation()
    setup_facial_expressions()
""",
            description="Système d'animation automatique pour personnages K-pop",
            compatibilite="Blender 3.0+ avec Rigify"
        )
        scripts.append(animation_script)
        
        self.blender_scripts = scripts
        return scripts

    def estimate_budget(self) -> BudgetEstimate:
        """Estimation budgétaire automatique"""
        
        # Calculs basés sur l'industrie de l'animation 3D
        pre_prod = 2500  # Concept art, storyboard, pré-viz
        production = 8000  # Animation 3D, rendu, éclairage
        post_prod = 1500  # Montage, color grading, audio
        materiel = 1200  # Location matériel si nécessaire
        logiciels = 800   # Licences Blender (gratuit), plugins, etc.
        
        total = pre_prod + production + post_prod + materiel + logiciels
        
        return BudgetEstimate(
            pre_production=pre_prod,
            production=production,
            post_production=post_prod,
            materiel=materiel,
            logiciels=logiciels,
            total=total
        )

    def export_pdf_professional(self, config: ExportConfig) -> str:
        """Export PDF ultra-professionnel"""
        
        if not REPORTLAB_AVAILABLE:
            return self._export_html_fallback(config)
        
        filename = f"court_metrage_kpop_production_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
        filepath = self.project_path / "pdf_reports" / filename
        
        # Configuration du document
        doc = SimpleDocTemplate(
            str(filepath),
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#FF69B4'),
            alignment=1  # Centré
        )
        
        content = []
        
        # Page de titre
        content.append(Paragraph("COURT-MÉTRAGE", title_style))
        content.append(Paragraph("Petite Fille K-pop à Salta", title_style))
        content.append(Spacer(1, 20))
        content.append(Paragraph("Dossier de Production Complet", styles['Heading2']))
        content.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
        content.append(Spacer(1, 50))
        
        # Résumé exécutif
        content.append(Paragraph("RÉSUMÉ EXÉCUTIF", styles['Heading2']))
        resume = """
        Court-métrage d'animation 3D de 36 secondes racontant l'histoire touchante d'une petite fille 
        argentine passionnée de K-pop. Le projet mélange modernité coréenne et authenticité sud-américaine 
        dans un style visuel Pixar. Budget estimé: 14,000€. Production: 8-12 semaines.
        """
        content.append(Paragraph(resume, styles['Normal']))
        content.append(Spacer(1, 30))
        
        # Analyse des shots
        if config.include_shots:
            content.append(Paragraph("ANALYSE DÉTAILLÉE DES SHOTS", styles['Heading2']))
            
            shots_data = [
                ['Shot', 'Durée', 'Description', 'Intensité', 'Plans suggérés'],
                ['1', '8s', 'Préparation danse', '6/10', '3 plans'],
                ['2', '12s', 'Explosion joie', '9/10', '4 plans'],
                ['3', '10s', 'Concentration', '8/10', '3 plans'],
                ['4', '6s', 'Interruption', '5/10', '3 plans'],
            ]
            
            shots_table = Table(shots_data)
            shots_table.setStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF69B4')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
            content.append(shots_table)
            content.append(Spacer(1, 20))
        
        # Budget
        if config.include_budget:
            budget = self.estimate_budget()
            content.append(Paragraph("ESTIMATION BUDGÉTAIRE", styles['Heading2']))
            
            budget_data = [
                ['Poste', 'Montant (€)'],
                ['Pré-production', f'{budget.pre_production:.0f}'],
                ['Production', f'{budget.production:.0f}'],
                ['Post-production', f'{budget.post_production:.0f}'],
                ['Matériel', f'{budget.materiel:.0f}'],
                ['Logiciels', f'{budget.logiciels:.0f}'],
                ['TOTAL', f'{budget.total:.0f}'],
            ]
            
            budget_table = Table(budget_data)
            budget_table.setStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00FFFF')),
                ('BACKGROUND', (-1, -1), (-1, -1), colors.HexColor('#FFD700')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (-1, -1), (-1, -1), 'Helvetica-Bold'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])
            content.append(budget_table)
        
        # Construction du PDF
        doc.build(content)
        
        return f"PDF professionnel généré: {filepath}"

    def _export_html_fallback(self, config: ExportConfig) -> str:
        """Export HTML si ReportLab non disponible"""
        
        filename = f"court_metrage_kpop_report_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
        filepath = self.project_path / "pdf_reports" / filename
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Court-Métrage K-pop Salta - Rapport</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                h1 {{ color: #FF69B4; text-align: center; }}
                h2 {{ color: #00FFFF; border-bottom: 2px solid #FFD700; }}
                .budget {{ background: #f0f0f0; padding: 20px; border-radius: 10px; }}
                .shot {{ background: #fff8dc; margin: 10px 0; padding: 15px; border-left: 5px solid #FF69B4; }}
            </style>
        </head>
        <body>
            <h1>Court-Métrage: Petite Fille K-pop à Salta</h1>
            <h2>Rapport de Production Complet</h2>
            <p><strong>Généré le:</strong> {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
            
            <h2>Résumé Exécutif</h2>
            <p>Court-métrage d'animation 3D innovant mélangeant culture K-pop et authenticité argentine. 
            Durée: 36 secondes. Style: Animation 3D moderne type Pixar.</p>
            
            <div class="budget">
                <h2>Estimation Budgétaire</h2>
                <p><strong>Budget total estimé: 14,000€</strong></p>
                <ul>
                    <li>Pré-production: 2,500€</li>
                    <li>Production: 8,000€</li>
                    <li>Post-production: 1,500€</li>
                    <li>Matériel: 1,200€</li>
                    <li>Logiciels: 800€</li>
                </ul>
            </div>
            
            <h2>Planning de Production</h2>
            <p><strong>Durée totale estimée:</strong> 8-12 semaines</p>
            <ul>
                <li><strong>Semaines 1-2:</strong> Pré-production (concept art, storyboard)</li>
                <li><strong>Semaines 3-8:</strong> Production 3D (modélisation, animation, rendu)</li>
                <li><strong>Semaines 9-10:</strong> Post-production (montage, audio)</li>
                <li><strong>Semaines 11-12:</strong> Finalisation et livraison</li>
            </ul>
        </body>
        </html>
        """
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return f"Rapport HTML généré: {filepath}"

    def generate_music_sync_files(self) -> Dict[str, str]:
        """Génère les fichiers de synchronisation musicale"""
        
        sync_files = {}
        
        # Timeline XML pour Premiere Pro
        premiere_xml = """<?xml version="1.0" encoding="UTF-8"?>
<xmeml version="5">
    <sequence>
        <name>Kpop_Salta_Timeline</name>
        <duration>1080</duration>
        <rate>
            <timebase>24</timebase>
        </rate>
        <media>
            <video>
                <track>
                    <clipitem>
                        <name>Shot_01_Preparation</name>
                        <start>0</start>
                        <end>192</end>
                        <file>
                            <name>Shot_01.mov</name>
                            <duration>192</duration>
                        </file>
                    </clipitem>
                    <clipitem>
                        <name>Shot_02_Dance</name>
                        <start>192</start>
                        <end>480</end>
                        <file>
                            <name>Shot_02.mov</name>
                            <duration>288</duration>
                        </file>
                    </clipitem>
                </track>
            </video>
            <audio>
                <track>
                    <clipitem>
                        <name>Kpop_Track</name>
                        <start>192</start>
                        <end>480</end>
                        <file>
                            <name>kpop_song.wav</name>
                            <duration>288</duration>
                        </file>
                    </clipitem>
                </track>
            </audio>
        </media>
        <marker>
            <name>Beat_1</name>
            <in>192</in>
            <out>192</out>
        </marker>
        <marker>
            <name>Beat_2</name>
            <in>216</in>
            <out>216</out>
        </marker>
    </sequence>
</xmeml>"""
        
        premiere_file = self.project_path / "music_sync" / "premiere_timeline.xml"
        with open(premiere_file, 'w', encoding='utf-8') as f:
            f.write(premiere_xml)
        sync_files["Premiere Pro"] = str(premiere_file)
        
        # JSON pour DaVinci Resolve
        resolve_json = {
            "timeline": {
                "name": "Kpop_Salta_Master",
                "framerate": 24,
                "clips": [
                    {
                        "name": "Shot_01",
                        "start_frame": 0,
                        "end_frame": 192,
                        "media_type": "video"
                    },
                    {
                        "name": "Kpop_Audio",
                        "start_frame": 192,
                        "end_frame": 480,
                        "media_type": "audio",
                        "tempo": 128,
                        "beat_markers": [192, 216, 240, 264, 288]
                    }
                ]
            }
        }
        
        resolve_file = self.project_path / "music_sync" / "resolve_timeline.json"
        with open(resolve_file, 'w', encoding='utf-8') as f:
            json.dump(resolve_json, f, indent=2)
        sync_files["DaVinci Resolve"] = str(resolve_file)
        
        return sync_files

    def save_all_scripts(self):
        """Sauvegarde tous les scripts Blender générés"""
        
        for script in self.blender_scripts:
            script_path = self.project_path / "blender_scripts" / script.nom_script
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script.code_python)
        
        # Fichier README pour les scripts
        readme_content = """# Scripts Blender - Court-Métrage K-pop Salta

## Installation
1. Ouvrir Blender 3.0+
2. Aller dans Scripting workspace
3. Ouvrir et exécuter les scripts dans l'ordre

## Scripts disponibles:
- `camera_movements_kpop.py`: Configuration automatique des caméras
- `character_animation_kpop.py`: Animation de base pour personnages

## Notes:
- Compatible Blender 3.0+
- Nécessite un personnage avec armature pour l'animation
- Les scripts sont optimisés pour le rendu Cycles/Eevee
"""
        
        readme_path = self.project_path / "blender_scripts" / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

    def generate_complete_project(self) -> Dict[str, Any]:
        """Génère le projet complet avec tous les outils"""
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "project_name": "Court-Métrage K-pop Salta",
            "version": "3.0"
        }
        
        # Génération des prompts IA
        ai_prompts = self.generate_ai_image_prompts()
        results["ai_prompts"] = len(ai_prompts)
        
        # Scripts Blender
        blender_scripts = self.generate_blender_scripts()
        self.save_all_scripts()
        results["blender_scripts"] = len(blender_scripts)
        
        # Synchronisation musicale
        sync_files = self.generate_music_sync_files()
        results["music_sync_files"] = list(sync_files.keys())
        
        # Estimation budgétaire
        budget = self.estimate_budget()
        results["estimated_budget"] = budget.total
        
        # Export PDF
        export_config = ExportConfig()
        pdf_result = self.export_pdf_professional(export_config)
        results["pdf_export"] = pdf_result
        
        # Sauvegarde des prompts IA
        prompts_file = self.project_path / "ai_generated" / "image_prompts.json"
        with open(prompts_file, 'w', encoding='utf-8') as f:
            json.dump([asdict(prompt) for prompt in ai_prompts], f, indent=2, ensure_ascii=False)
        
        return results

def main():
    """Fonction principale - Interface en ligne de commande"""
    
    print("🎬 Script Analyzer V3.0 - Court-Métrage K-pop Salta")
    print("=" * 60)
    
    analyzer = ScriptAnalyzerV3()
    
    while True:
        print("\n🎛️  Que voulez-vous faire ?")
        print("1. 🤖 Générer prompts IA pour images")
        print("2. 🎮 Créer scripts Blender")
        print("3. 📄 Export PDF professionnel")
        print("4. 🎵 Synchronisation musicale")
        print("5. 💰 Estimation budgétaire")
        print("6. 🚀 Génération complète du projet")
        print("7. ❌ Quitter")
        
        choix = input("\nVotre choix (1-7): ").strip()
        
        if choix == "1":
            print("\n🤖 Génération des prompts IA...")
            prompts = analyzer.generate_ai_image_prompts()
            print(f"✅ {len(prompts)} prompts générés!")
            for prompt in prompts:
                print(f"   • {prompt.titre}")
            
        elif choix == "2":
            print("\n🎮 Création des scripts Blender...")
            scripts = analyzer.generate_blender_scripts()
            analyzer.save_all_scripts()
            print(f"✅ {len(scripts)} scripts créés!")
            for script in scripts:
                print(f"   • {script.nom_script}")
        
        elif choix == "3":
            print("\n📄 Export PDF professionnel...")
            config = ExportConfig()
            result = analyzer.export_pdf_professional(config)
            print(f"✅ {result}")
        
        elif choix == "4":
            print("\n🎵 Génération fichiers de sync musical...")
            sync_files = analyzer.generate_music_sync_files()
            print("✅ Fichiers créés:")
            for software, filepath in sync_files.items():
                print(f"   • {software}: {filepath}")
        
        elif choix == "5":
            print("\n💰 Estimation budgétaire...")
            budget = analyzer.estimate_budget()
            print("✅ Estimation complète:")
            print(f"   • Pré-production: {budget.pre_production:.0f}€")
            print(f"   • Production: {budget.production:.0f}€")
            print(f"   • Post-production: {budget.post_production:.0f}€")
            print(f"   • Matériel: {budget.materiel:.0f}€")
            print(f"   • Logiciels: {budget.logiciels:.0f}€")
            print(f"   📊 TOTAL: {budget.total:.0f}€")
        
        elif choix == "6":
            print("\n🚀 Génération complète du projet...")
            print("⏳ Ceci peut prendre quelques minutes...")
            
            results = analyzer.generate_complete_project()
            
            print("✅ PROJET COMPLET GÉNÉRÉ!")
            print(f"   • Prompts IA: {results['ai_prompts']}")
            print(f"   • Scripts Blender: {results['blender_scripts']}")
            print(f"   • Sync musicale: {len(results['music_sync_files'])}")
            print(f"   • Budget estimé: {results['estimated_budget']:.0f}€")
            print(f"   • Export PDF: ✅")
            print(f"\n🎯 Votre court-métrage est prêt pour la production!")
        
        elif choix == "7":
            print("\n👋 Au revoir ! Bon succès avec votre court-métrage K-pop !")
            break
        
        else:
            print("❌ Choix invalide. Veuillez choisir entre 1 et 7.")

if __name__ == "__main__":
    main()
