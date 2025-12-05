"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class AudioFeatures {
    constructor(features) {
        this.defaults = { min: 0, max: 1, total: 0, count: 0, avg: 0 };
        this.acousticness = Object.assign(Object.assign({}, this.defaults), { label: 'Acousticness' });
        this.danceability = Object.assign(Object.assign({}, this.defaults), { label: 'Danceability' });
        this.energy = Object.assign(Object.assign({}, this.defaults), { label: 'Engery' });
        this.instrumentalness = Object.assign(Object.assign({}, this.defaults), { label: 'Instrumentalness' });
        this.loudness = Object.assign(Object.assign({}, this.defaults), { label: 'Loudness', min: -100, max: 0 });
        this.liveness = Object.assign(Object.assign({}, this.defaults), { label: 'Liveness' });
        this.speechiness = Object.assign(Object.assign({}, this.defaults), { label: 'Speechiness' });
        this.tempo = Object.assign(Object.assign({}, this.defaults), { label: 'Tempo', min: 0, max: 1015 });
        this.valence = Object.assign(Object.assign({}, this.defaults), { label: 'Valence' });
        this.metrics = {};
        this.metrics = {};
        if (features === null || features === void 0 ? void 0 : features.length) {
            features.forEach(feature => {
                Object.keys(feature).forEach(key => {
                    if (this[key]) {
                        this[key].total += feature[key];
                        this[key].count += 1;
                        this[key].avg = parseFloat(this[key].total) / this[key].count;
                        this.metrics[key] = this[key];
                    }
                });
            });
        }
    }
    getMetrics() {
        return this.metrics;
    }
    getFeaturesForRecommendations() {
        const recommendationFeatures = {};
        Object.keys(this.metrics).forEach(key => {
            if (key !== 'tempo') {
                recommendationFeatures[`target_${key}`] = this.metrics[key].avg;
            }
        });
        return recommendationFeatures;
    }
}
exports.default = AudioFeatures;
//# sourceMappingURL=AudioFeatures.js.map