/**
 * Находит размеры коробок для обмена, чтобы у Алисы и Боба стало поровну конфет.
 *
 * Алгоритм:
 * - Вычисляем общую сумму конфет у Алисы и Боба.
 * - Находим разницу diff = (sumA - sumB) / 2.
 * - Для каждой коробки Алисы a вычисляем необходимую коробку Боба b = a - diff.
 * - Если b есть у Боба (хранится в множестве), возвращаем [a, b].
 *
 * @param {number[]} aliceSizes - массив коробок Алисы
 * @param {number[]} bobSizes   - массив коробок Боба
 * @returns {number[]} - массив из двух чисел [коробка_Алисы, коробка_Боба]
 */
var fairCandySwap = function(aliceSizes, bobSizes) {
    let sumA = aliceSizes.reduce((a,b)=>a+b, 0);
    let sumB = bobSizes.reduce((a,b)=>a+b, 0);
    let diff = (sumA - sumB) / 2;
    let setB = new Set(bobSizes);
    for (let a of aliceSizes) {
        let need = a - diff;
        if (setB.has(need))
            return [a, need];
    }
};