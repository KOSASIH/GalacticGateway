const tf = require('@tensorflow/tfjs');

class GalacticAIModel {
    constructor() {
        this.model = tf.sequential();
        this.model.add(tf.layers.dense({ units: 1, inputShape: [1] }));
        this.model.compile({ optimizer: tf.optimizers.adam(), loss: 'meanSquaredError' });
    }

    async predict(input) {
        return this.model.predict(input);
    }
}

module.exports = GalacticAIModel;
