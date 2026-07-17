import {loadLayersModel} from '@tensorflow/tfjs'

export async function loadModel() {
  return await loadLayersModel('/model/model.json');
}
