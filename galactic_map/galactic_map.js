import * as THREE from "three";

class GalacticMap {
    constructor(container) {
        this.container = container;
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, container.offsetWidth / container.offsetHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({
            canvas: container,
            antialias: true
        });

        // Load galaxy data from a JSON file
        fetch("galaxy_data.json")
           .then(response => response.json())
           .then(data => {
                this.generateGalaxy(data);
            });
    }

    generateGalaxy(data) {
        // Create a galaxy mesh using the loaded data
        const galaxyMesh = new THREE.Mesh(
            new THREE.SphereGeometry(100, 60, 60),
            new THREE.MeshBasicMaterial({
                map: new THREE.TextureLoader().load("galaxy_texture.jpg")
            })
        );

        // Add stars, planets, and other celestial bodies to the scene
        data.stars.forEach(star => {
            const starMesh = new THREE.Mesh(
                new THREE.SphereGeometry(0.1, 10, 10),
                new THREE.MeshBasicMaterial({
                    color: star.color
                })
            );
            starMesh.position.set(star.x, star.y, star.z);
            this.scene.add(starMesh);
        });

        // Render the scene
        this.renderer.render(this.scene, this.camera);
    }
}

// Example usage
const container = document.getElementById("galactic-map");
const galacticMap = new GalacticMap(container);
