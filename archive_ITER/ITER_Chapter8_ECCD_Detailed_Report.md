# ITER Physics Basis Chapter 8 詳細分析レポート

## ECCD/ECRH仕様およびプラズマ運転制御

**分析日**: 2026年3月2日  
**分析対象**:

- Chapter 6: Plasma auxiliary heating and current drive (Nuclear Fusion 39, 2495-2539, 1999)
- Chapter 8: Plasma operation and control (Nuclear Fusion 39, 2577-2638, 1999)

---

## エグゼクティブサマリー

ITER Physics Basis（1999年版）のChapter 8「Plasma operation and control」およびChapter 6「Plasma auxiliary heating and current drive」から、ECCD/ECRH（電子サイクロトロン電流駆動/加熱）システムの詳細仕様、プラズマ運転シナリオ、制御戦略を抽出・分析した。

**主要な発見**：

- **ECRF周波数**: 170 GHz（メインシステム）、90-140 GHz（start-upシステム）
- **総パワー**: 50 MW（定常運転）、3 MW（start-up assist）
- **システム効率**: 30-40%
- **電流駆動効率**: η₂₀ = 0.16-0.19 A·W⁻¹·m⁻² (170 GHz)、最大0.3-0.33 (230 GHz)
- **プラズマ制御**: 磁気制御 + kinetics制御の統合システム

---

## 1. 分析したPDFファイル

### 1.1 Chapter 6: Plasma auxiliary heating and current drive

- **ファイル名**: ITER_Physics_Expert_Group_on_Energetic_Particles,_Heating_and_Current_Drive_1999_Nucl._Fusion_39_2495.pdf
- **総ページ数**: 46ページ
- **ECCD関連ページ**: 14ページ
- **著者**: ITER Physics Expert Group on Energetic Particles, Heating and Current Drive
- **Chair**: J. Jacquinot (JET), S. Putvinski (ITER JCT, co-chair)

### 1.2 Chapter 8: Plasma operation and control

- **ファイル名**: ITER_Physics_Expert_Group_on_Disruptions,_Plasma_Control,_and_MHD_1999_Nucl._Fusion_39_2577.pdf
- **総ページ数**: 50ページ
- **ECCD/制御関連ページ**: 13ページ
- **著者**:
  - ITER Physics Expert Group on Disruptions, Plasma Control, and MHD
  - ITER Physics Expert Group on Energetic Particles, Heating and Current Drive
  - ITER Physics Expert Group on Diagnostics

---

## 2. ECCD/ECRH システム詳細仕様

### 2.1 周波数仕様

#### 2.1.1 メインECRFシステム

- **選択周波数**: **170 GHz**（固定周波数ジャイロトロン）
- **最適動作範囲**: 160-230 GHz（フルフィールド5.7 T時）
- **物理的根拠**:
  - 加熱位置: r/a = 0.15（垂直入射時、メジャーアクシスよりわずかに内側）
  - オハミック相（Te0 = 5 keV, ne0 = 3×10¹⁹ m⁻³）から点火相まで完全吸収
  - 光学的厚さ（opacity）: 30-300（強く局所化された吸収）

#### 2.1.2 Start-upアシストシステム

- **周波数範囲**: **90-140 GHz**
- **目的**:
  - Pre-ionization
  - Burnthrough assist
  - 広範なトロイダル磁場条件への対応
- **パワー**: 3 MW（吸収パワー）
- **パルス長**: 数秒（burnthroughを確保するのに十分）

### 2.2 パワー仕様

| システム             | パワー | 運転モード    | 効率   | 備考                      |
| -------------------- | ------ | ------------- | ------ | ------------------------- |
| **ECRF（ITER要求）** | 50 MW  | 定常運転 (SS) | 30-40% | Equatorial portから入射   |
| **ECRF（実証済み）** | 2.8 MW | 0.2 s         | 30-40% | 既存トカマク (28-157 GHz) |
| **Start-up ECRH**    | 3 MW   | 数秒          | -      | Burnthrough保証           |

### 2.3 電流駆動効率

#### 2.3.1 効率の定義

```bash
η₂₀ = <ne20> × IECCD × R0 / Plaunched
```

- <ne20>: 体積平均電子密度 [10²⁰ m⁻³]
- IECCD: EC駆動電流 [A]
- R0: 主半径（磁気軸位置） [m]
- Plaunched: 入射ECパワー [W]

#### 2.3.2 ITER予測効率

| 条件      | 周波数  | Te0    | トロイダル角 | η₂₀ [A·W⁻¹·m⁻²] |
| --------- | ------- | ------ | ------------ | --------------- |
| Reference | 170 GHz | 20 keV | 最適角       | 0.16            |
| Reference | 170 GHz | 30 keV | 最適角       | 0.19            |
| Optimized | 230 GHz | 30 keV | 40°          | 0.28-0.33       |
| Low field | 170 GHz | 30 keV | 最適角       | 0.30            |

**低磁場運転** (B = 4.2 T): η₂₀ ≈ 0.3 A·W⁻¹·m⁻²

#### 2.3.3 実験結果との比較

| トカマク     | Te     | η₂₀ [10²⁰ A·W⁻¹·m⁻²] | スキーム                  |
| ------------ | ------ | -------------------- | ------------------------- |
| RTP          | ~3 keV | 0.01                 | Upshifted/Downshifted     |
| DIII-D       | ~3 keV | 0.015                | Downshifted (synergy含む) |
| T-10         | ~7 keV | 0.03                 | Upshifted                 |
| **ITER予測** | 30 keV | **0.3**              | Upshifted O-mode          |

**温度依存性**: 効率はTe0 = 30 keVで最大化、それ以上では温度依存性が弱い

### 2.4 ECCD方式

#### 2.4.1 Upshifted Scheme（ITER採用）

- **入射方式**: LFS（Low Field Side）mid-plane から Ordinary Mode (O-mode)
- **偏光**: 楕円偏光O-mode
- **物理機構**:
  - LFS共鳴の高磁場側で吸収
  - Nk > 0 の電子を選択的加熱
  - 大きな光学的厚さにより高効率
- **利点**:
  - X-mode cutoffを回避
  - Second harmonic吸収の大幅削減
  - 吸収位置の良好な制御性

#### 2.4.2 Downshifted Scheme（参考）

- **入射方式**: HFS（High Field Side）から X-mode
- **実証**: DIII-D, COMPASS-D, RTP
- **問題点**: ITERでは幾何学的制約があり採用せず

### 2.5 ジャイロトロン技術開発目標

| パラメータ     | 目標値                           | 現状               |
| -------------- | -------------------------------- | ------------------ |
| **周波数**     | 170 GHz                          | 28-157 GHz実証済み |
| **出力パワー** | 1 MW                             | 2.8 MW (0.2 s)     |
| **運転モード** | 定常運転 (Steady State)          | 0.2 s実証          |
| **効率**       | 50%                              | 30-40%             |
| **コレクタ**   | Single stage depressed collector | 開発中             |
| **ウィンドウ** | ダイヤモンド（最大2 MW可能）     | 開発中             |

**ウィンドウ技術オプション**:

1. 室温シングルディスク、エッジ冷却ダイヤモンドウィンドウ
2. Au添加高抵抗シリコンウィンドウ（冷却）
3. 極低温ウィンドウ
4. 分散ウィンドウ

### 2.6 ランチャー配置

- **位置**: LFS mid-plane
- **距離**: ブランケット/バックプレート後方 約1 m（プラズマから）
- **理由**:
  - ECは真空中を伝搬するため、プラズマ近傍である必要はない
  - しかし、必要なステアリング能力を確保するため、遠すぎてもいけない
- **ステアリング**: トロイダル方向の斜入射角度可変
- **ポート**: Single equatorial port

---

## 3. プラズマ運転シナリオ

### 3.1 Reference Operation Scenario（21 MA燃焼プラズマ）

#### 3.1.1 主要フィデューシャルポイント

```bash
Initiation (0.5 MA) → Magnetization → XPF (15 MA) → SOF (21 MA) → SOB → EOB → Current Ramp-down
```

- **Initiation**: 0.5 MA（初期breakdown）
- **XPF**: 15 MA（X-point形成、リミター→ダイバータ遷移）
- **SOF** (Start of Flat-top): 21 MA（フラットトップ開始）
- **SOB** (Start of Burn): 燃焼開始
- **EOB** (End of Burn): 燃焼終了

#### 3.1.2 電流立ち上げ波形

| フェーズ     | 電流範囲     | 立ち上げ率 | 時間  |
| ------------ | ------------ | ---------- | ----- |
| 初期立ち上げ | 0.5 → 約5 MA | 0.2 MA/s   | ~22 s |
| 中間立ち上げ | 約5 → 14 MA  | 0.16 MA/s  | ~56 s |
| X-point形成  | 14 → 15 MA   | 0.05 MA/s  | ~20 s |
| 最終立ち上げ | 15 → 21 MA   | 0.10 MA/s  | ~60 s |

**総magnetization時間**: 約150-200秒

#### 3.1.3 MHD安定性制約（li-q空間）

電流立ち上げは **li-q安定領域** を維持しながら実行：

- **内部インダクタンス li**: 制御範囲内に維持
- **q95**: 安全係数を適切に維持
- **目的**: 内部MHD不安定性と密度限界破壊を回避

### 3.2 Plasma Initiation（プラズマ起動）

#### 3.2.1 Townsend Breakdown条件

**最小電場**:

```bash
Emin = B × p / ln[A × p × L]
```

- p: pre-fill圧力 [Torr]
- L: 有効接続長 [m]
- A, B: ガス種依存係数

**水素/重水素**:

- A = 510 m⁻¹·Torr⁻¹
- B = 1.25×10⁴ V·m⁻¹·Torr⁻¹
- Emin = 0.04-0.4 V/m (L = 200-2000 m)

**ヘリウム**:

- A = 300 m⁻¹·Torr⁻¹
- B = 3.4×10⁴ V·m⁻¹·Torr⁻¹
- より高いEmin（低電場start-upには不利）

**最適pre-fill圧力**: 5×10⁻⁶ - 5×10⁻⁵ Torr

**信頼性のあるbreakdown条件**: E ≥ 2 × Emin

#### 3.2.2 ITER Start-up仕様

| パラメータ        | 値        | 備考                       |
| ----------------- | --------- | -------------------------- |
| **誘導電場**      | 0.3 V/m   | チャンバー内               |
| **ループ電圧**    | ~3 V/turn | 1ターンあたり              |
| **ECRH assist**   | 3 MW吸収  | 90-140 GHz                 |
| **Breakdown時間** | <3 ms     | ECRH使用時                 |
| **信頼性向上**    | 大幅改善  | 磁場null品質への許容度向上 |

#### 3.2.3 ECRH Assisted Start-up実証

**DIII-D実績**:

- ECパワー: 700 kW @ 60 GHz
- 最小電場: **0.15 V/m** (1.6 V/turn)
- Breakdown時間: ~30 ms（低E場）→ <3 ms（ECRH使用）
- runaway電子生成: 大幅抑制

**JT-60U実績**:

- LHRFアシスト: 1.5 MW @ 1.7-2.4 GHz
- 最小電場: **0.08 V/m**
- Pre-fill gas: ヘリウム（不純物に強い）

### 3.3 Burnthrough（電離突破）

#### 3.3.1 物理的要求

**完全電離達成条件**:

1. 水素の完全電離
2. 不純物の高電離状態への遷移
3. 放射損失の克服

#### 3.3.2 ITER Burnthrough仕様

| 条件                  | 要求   | 対策                           |
| --------------------- | ------ | ------------------------------ |
| **ベリリウム不純物**  | 最大5% | 3 MW ECRH で良好なstart-up     |
| **カーボン不純物**    | 5%     | 5 MW ECRH でもmargin限定的     |
| **重水素密度制御**    | 重要   | vessel体積/プラズマ体積比が大  |
| **中性粒子screening** | 重要   | 電離領域外からのfuellingを考慮 |

**ECRHパルス長**: 数秒（burnthroughを確保するのに十分）

#### 3.3.3 波動吸収機構（低温初期プラズマ）

- **O-mode入射**: 低電子温度でも効率的
- **斜入射**: トロイダル方向に傾けた入射
- **mode conversion**: 内壁反射時にO-mode → X-mode変換
- **複数反射**: 数回の反射後、75%以上の吸収を期待

### 3.4 抵抗性flux消費（Ejima式）

#### 3.4.1 Ejima公式

```bash
Ψres = CEjima × μ0 × R0 × Ip
```

**設計用係数**: CEjima = **0.45**

| CEjima値  | 条件           | 備考                             |
| --------- | -------------- | -------------------------------- |
| 0.40      | 理論的最小値   | q=3プラズマ                      |
| 0.45      | 設計推奨値     | 実用的最小flux消費               |
| 0.40-0.50 | 実験データ範囲 | 既存トカマク                     |
| >0.50     | 非最適条件     | 遅すぎる立ち上げ、非最適半径拡大 |

#### 3.4.2 補助加熱の効果

**重要な知見**:

- 電流立ち上げ中の補助加熱は **総抵抗損失を削減しない**
- 効果: 抵抗損失の発生を **遅延** させるのみ
- 完全に貫通した電流分布達成時に、結局同じfluxを消費
- 利点: 電流分布平衡化の時間を増やす（ELMy H-mode放電に適切）

### 3.5 電流分布制御とAdvanced Scenarioへの貢献

#### 3.5.1 Reverse Shear q-profile生成

**制御アクチュエータの統合**:

- PF磁場形状制御
- 非誘導電流駆動（ECCD, LHCD）
- 補助加熱パワー
- 電流ランプ制御

**目標**:

- Internal Transport Barrier (ITB)の生成と制御
- q0 > 1（中心安全係数を1以上に維持）
- Bootstrap電流の最大化

#### 3.5.2 ECCD役割

| 適用                | ECCD役割           | 要求効率                     |
| ------------------- | ------------------ | ---------------------------- |
| **On-axis CD**      | 中心q値制御        | 容易に達成可能               |
| **Off-axis CD**     | >2 MA @ 低Te       | 理論CD効率限界近くで動作必要 |
| **Current profile** | j(r)のテーラリング | LHCD/ECCDの組み合わせ最適    |

---

## 4. フィードバック制御系

### 4.1 磁気制御（Magnetics Control）

#### 4.1.1 物理的基礎

**Grad-Shafranov平衡方程式**:

- 2次元磁気静水圧平衡
- 質量流、プラズマ回転、圧力異方性を無視
- PFコイル電流、プラズマ圧力分布、電流分布、トロイダル磁場から決定

**制御パラメータ**:

- βp（規格化プラズマ圧力）
- li（内部インダクタンス）

これら2つのパラメータで、elongatedプラズマの静的flux面配置を正確に決定可能

#### 4.1.2 制御目標

| 制御対象                  | 精度要求           | 理由                     |
| ------------------------- | ------------------ | ------------------------ |
| **最外殻flux面位置**      | 高精度、高信頼性   | separatrixでの高熱流束   |
| **Divertor strike point** | 高精度             | ターゲット板保護         |
| **形状制御**              | 動的フィードバック | 擾乱への応答             |
| **長パルス運転**          | 最小制御動作       | 超伝導コイルのAC損失低減 |

#### 4.1.3 超伝導コイルの制約

**AC損失問題**:

- 連続的なdithering（制御パラメータの揺らぎ）
- プラズマ擾乱への応答
- 繰り返しELMsへの応答
→ 超伝導コイルと極低温構造の加熱

**対策**:

- より複雑なフィードバックコントローラ（adaptive/intelligent control）
- AC損失累積の制限

### 4.2 Kinetics Control（動力学制御）

#### 4.2.1 制御目標

**コアプラズマ属性**:

- 密度 (ne)
- 温度 (Te, Ti)
- 不純物含有量
- 電流密度 j(r)
- 核融合出力（DT プラズマ）

**Edge/Divertor属性**:

- 温度
- 密度
- 不純物含有量と電離状態
- 放射パワー
- PFCへの伝導・対流パワー

#### 4.2.2 制御アクチュエータ

| アクチュエータ               | 制御対象                  | 実施例                      |
| ---------------------------- | ------------------------- | --------------------------- |
| **Gas/Pellet fuelling**      | 密度 (ne, ne-bar)         | 全主要装置                  |
| **Gas injection (divertor)** | Edge密度、中性粒子圧      | DIII-D, ASDEX-Upgrade       |
| **Impurity gas injection**   | 放射分率                  | ASDEX-Upgrade, TEXTOR       |
| **Auxiliary power**          | 温度、核融合出力          | JT-60U（DD中性子）          |
| **NBI duty cycle**           | Wth, βN, MARFE抑制        | DIII-D, TFTR, ASDEX-Upgrade |
| **ECCD**                     | 電流分布 j(r)             | DIII-D（計画中）            |
| **LHCD launcher phasing**    | 電流分布 j(r)             | Tore-Supra                  |
| **Localized ECCD**           | Neoclassical tearing mode | ASDEX-Upgrade               |

#### 4.2.3 3つのパワー制御

**Kinetics制御の本質**: **3つのパワーの安定制御**

1. **核融合出力** (Pfusion)
   - 密度制御を通じて（点火プラズマ）
   - 補助加熱パワー制御

2. **Separatrixを横切るパワー流** (Psep)
   - H-mode閾値維持
   - 放射損失制御

3. **Divertor PFCへのパワー流** (Pdiv)
   - detachment制御
   - 熱負荷分散

**制約**: 密度が **Greenwald密度の1.5倍** を超えないこと

```bash
ne,20 ≤ 1.5 × (Ip,MA / πa²)
```

（経験的係数1.5は暫定的、物理的理解により置き換え予定）

### 4.3 統合制御（Integrated Control）

#### 4.3.1 Magnetics + Kinetics統合の必要性

**従来**: 明確な分離

- Magnetics: PF coil system
- Kinetics: Fuelling, heating, pumping

**Advanced tokamak運転**: 統合が必須

- 電流ランプ制御（PF + auxiliary heating）
- Internal Transport Barrier生成
- q-profile制御

#### 4.3.2 非線形制御の必要性

**Transport bifurcation access**:

1. **H-mode edge transition**
   - 閾値パワーPth（separatrixを横切るパワー）
   - 非線形遷移
2. **Internal Transport Barriers**
   - 電流分布制御との協調
   - Magnetics + kinetics統合制御
   - 定常運転への鍵

---

## 5. MHD制御手法

### 5.1 Tearing Mode制御（ECRFによる）

#### 5.1.1 物理的機構

**Tearing mode**: 抵抗性MHD不安定性

- ネストしたflux面の再結合
- 磁気島の生成
- 温度分布のflat spot → 蓄積エネルギー減少

**Neoclassical tearing mode**:

- Bootstrap電流の減少が駆動源
- 島が発達し、O-pointで圧力がflattenされるとbootstrap電流減少
- βlimitの現象の一つ
- m=2 modeがITERで最も重要な不安定性

#### 5.1.2 ECRF適用方法

**DCスキーム（連続入射）**:

- 平衡電流分布の整形
- 共鳴面近傍の自由エネルギー減少
- 安定性指数Δ'の制御
- 連続入射可能

**ACスキーム（位相制御入射）**:

- 島のO-pointに直接入射
- 局所的に失われた電流を回復
- 位相制御が必要

**実証実験**:

- JFT-2M: DCスキーム成功
- T-10: DCスキーム成功
- ASDEX-Upgrade: ACスキーム（位相制御ECCD）成功
- COMPASS-D: ACスキーム（位相フィードバックループ閉）成功

#### 5.1.3 ITER適用予測

**m=2 neoclassical tearing mode**:

- 周波数: 130 GHz（q=2面で最適）
- 入射角: 10-20度（比較的小角）
- 要求駆動電流: 総電流の約1%
- 目標: 島幅を吸収幅程度に縮小（完全除去は他の手段併用）

**最適化パラメータ**: IECCD / d²

- d: ECCD吸収幅
- 安定化効果は電流密度勾配に依存

**Locked mode対策**:

- 複数ポートからの入射（島のO-pointが常に照射可能）
- または外部コイルによるerror field補償

### 5.2 Sawtooth制御

#### 5.2.1 制御目的

**Sawtoothの役割**:

- 不純物とHe ashのコアからの輸送（有益）
- しかし繰り返し周波数の制御が必要（最大化）

#### 5.2.2 制御方式

**DCスキーム**:

- q=1面での局所DC電流駆動
- 平衡分布の制御
- 実証: JET（Ion cyclotron heating）
- ECCD: より局所化された吸収により、さらに有効

**ACスキーム**:

- m=1, n=1 precursor modeのO-pointへの局所電流駆動
- 成長率の変化 → sawtooth繰り返し時間の延長または短縮
- 理論的推定: m=2 modeより困難（ほぼideal resistive kinkの性質）

**課題**: 300 MW alpha powerとの競合 → 圧力分布制御は実現困難

### 5.3 ELM制御

#### 5.3.1 実験結果（DIII-D）

**Type I ELM**:

- エッジ加熱（separatrix内側） → ELM周波数増加
- エッジ加熱（separatrix外側） → ELM周波数減少

**メカニズム仮説**:

1. 抵抗率減少 → 電流拡散時間増大
2. Separatrix横断の圧力勾配のsoftening

**Type III ELM**:

- ECH適用 → ELM周波数減少（他の加熱手法と一貫）

**Type II ELM**: 実験データなし（edge加熱で制御可能な可能性）

**ITER適用**: ELM typeの予測が困難なため、有効性は不確実

---

## 6. 統合シミュレーション

### 6.1 使用コード

#### 6.1.1 Ray tracing / Fokker-Planck codes

**ECCD理論**: 高度に発達

- **CQL3D** [LLNL]
- **ORGAY**
- **BANDIT-3D**

**Benchmark結果**: 

- Neoclassical電気伝導率（解析解と一致）
- Low power, linear ECCD効率（adjoint計算と一致）
- DIII-D ECCD実験との定量的一致
- 異なるコード間の一致

**予測能力**:

- 現在の実験の予測可能
- ITERへの適用に自信

#### 6.1.2 Tokamak Simulation Code (TSC)

**機能**:

- プラズマシナリオモデリング
- 平衡応答のシミュレーション
- li-q空間でのtrajectory解析

**ITER Reference Scenario検証** (Figure 15):

- Current ramp-up: 0.5 MA → 21 MA
- li-q空間で常に安定領域に維持
- Ignition, burn, current ramp-downのフルシナリオ

### 6.2 非熱的効果の評価

**臨界パワー密度**:

```bash
P [MW/m³] / [n (10¹⁹ m⁻³)]² > 0.5  → 非熱的効果予想
```

**ITER条件**: ECパワー密度はこの臨界値を十分下回る
→ **非熱的効果は予想されない**

### 6.3 シミュレーション結果の検証

**Present tokamaks**:

- プラズマ平衡応答モデルの実験的検証は励まし的
- コントローラ設計の基礎として妥当

**ITER controller design simulations**:

- 予測応答は良好
- Intelligent/adaptive magnetics control の検証済み

---

## 7. 重要な数値データまとめ

### 7.1 ITERプラズマパラメータ（Reference Scenario）

| パラメータ               | 値        | 単位 | 備考            |
| ------------------------ | --------- | ---- | --------------- |
| **主半径 R0**            | 8.14      | m    | Major radius    |
| **小半径 a**             | 2.80      | m    | Minor radius    |
| **プラズマ電流 Ip**      | 21        | MA   | Nominal         |
| **トロイダル磁場 BT**    | 5.68      | T    | at R=8.14 m     |
| **電子密度 ne**          | 0.98×10²⁰ | m⁻³  |                 |
| **体積平均温度**         | 12.9      | keV  |                 |
| **中心温度 Te0**         | 20-30     | keV  | Flat-top時      |
| **βN**                   | 2.29      | -    | Normalized beta |
| **q95**                  | 3.0       | -    | Safety factor   |
| **核融合出力**           | 1.5       | GW   | Ignited         |
| **プラズマ熱エネルギー** | 1.07      | GJ   |                 |

### 7.2 ECCD/ECRHシステムパラメータ

| パラメータ                 | 値         | 備考                 |
| -------------------------- | ---------- | -------------------- |
| **メイン周波数**           | 170 GHz    | 固定周波数           |
| **Start-up周波数**         | 90-140 GHz | 可変範囲             |
| **メインパワー**           | 50 MW      | 定常運転             |
| **Start-upパワー**         | 3 MW       | 吸収パワー           |
| **ジャイロトロン単体出力** | 1 MW       | 開発目標             |
| **ジャイロトロン効率**     | 50%        | 開発目標             |
| **システム効率**           | 30-40%     | Wall plug → プラズマ |
| **電流駆動効率 η₂₀**       | 0.16-0.19  | A·W⁻¹·m⁻² @ 170 GHz  |
| **最大効率 η₂₀**           | 0.28-0.33  | A·W⁻¹·m⁻² @ 230 GHz  |

### 7.3 Start-upパラメータ

| パラメータ          | 値                   | 備考         |
| ------------------- | -------------------- | ------------ |
| **誘導電場**        | 0.3 V/m              | チャンバー内 |
| **ループ電圧**      | ~3 V/turn            |              |
| **ECRH assist**     | 3 MW                 | 吸収パワー   |
| **Breakdown時間**   | <3 ms                | ECRH使用時   |
| **Pre-fill圧力**    | 5×10⁻⁶ - 5×10⁻⁵ Torr | 最適範囲     |
| **CEjima係数**      | 0.45                 | 設計推奨値   |
| **Burnthrough時間** | 数秒                 | ECRH必要     |

### 7.4 制御システム時定数・精度

| パラメータ            | 値/要求            | 備考            |
| --------------------- | ------------------ | --------------- |
| **位置制御精度**      | cm order           | separatrix位置  |
| **Strike point精度**  | cm order           | Divertor保護    |
| **密度制御範囲**      | < 1.5 × nGreenwald | Greenwald limit |
| **AC損失許容**        | 制限あり           | 長パルス時重要  |
| **Magnetics応答時間** | ms order           | フィードバック  |
| **Kinetics応答時間**  | s order            | 典型的          |

---

## 8. ITER実装への推奨事項

### 8.1 システム設計推奨

#### 8.1.1 ECCD/ECRHシステム

**優先度1（必須）**:

1. **170 GHz, 1 MW ジャイロトロン × 50台**
   - 定常運転、50%効率
   - Single stage depressed collector
   - ダイヤモンドウィンドウ（各1-2 MW対応）

2. **Start-up assist system: 3 MW @ 90-140 GHz**
   - 周波数可変または複数周波数
   - reliableなbreakdownとburnthrough確保

3. **LFS mid-plane launcher**
   - Equatorial port配置
   - トロイダル角度ステアリング: 0-60度
   - Poloidal角度ステアリング追加が望ましい

**優先度2（強く推奨）**:

4. **MHD制御用dedicated system**
   - 130 GHz（q=2面最適）
   - 局所化された吸収（小入射角）
   - 複数ポート入射または位相制御

1. **Off-axis current drive capability**
   - LHCDとの組み合わせ
   - r/a > 0.5での効率的CD

#### 8.1.2 制御システム

**Magnetics Control**:

1. Adaptive/intelligent controller実装
2. AC損失monitoring and limitation
3. Real-time equilibrium reconstruction
4. Strike point位置フィードバック

**Kinetics Control**:

1. 3-power制御アルゴリズム（Pfusion, Psep, Pdiv）
2. 密度フィードバック（pellet + gas injection）
3. 放射分率制御（impurity gas injection）
4. NBI duty cycle制御

**Integrated Control**:

1. Magnetics + Kinetics協調制御
2. Current profile制御（ECCD + LHCD + NBI）
3. ITB生成・維持シーケンス
4. Advanced scenario自動化

### 8.2 研究開発優先課題

#### 8.2.1 技術開発（高優先度）

| 課題                       | 現状          | 目標                | 重要度 |
| -------------------------- | ------------- | ------------------- | ------ |
| **170 GHz, 1MW gyrotron**  | 2.8 MW @ 0.2s | 1 MW SS @ 50%       | ★★★★★  |
| **ダイヤモンドウィンドウ** | 開発中        | 2 MW, SS            | ★★★★★  |
| **Depressed collector**    | 開発中        | 50%効率達成         | ★★★★☆  |
| **Launcher steering**      | 設計中        | Toroidal + poloidal | ★★★★☆  |

#### 8.2.2 物理実証（高優先度）

| 課題                      | 現状           | 必要な実証                | 重要度 |
| ------------------------- | -------------- | ------------------------- | ------ |
| **Off-axis ECCD**         | 限定的データ   | Medium size tokamakで実証 | ★★★★★  |
| **Neoclassical mode制御** | 原理実証       | Long pulse実証            | ★★★★☆  |
| **ITB制御**               | 一部実証       | 再現性、制御性実証        | ★★★★☆  |
| **ELM制御**               | メカニズム不明 | Type I, II, III詳細研究   | ★★★☆☆  |

#### 8.2.3 統合シミュレーション（高優先度）

| 課題                             | 推奨アクション                                 |
| -------------------------------- | ---------------------------------------------- |
| **Full scenario simulation**     | TSC + transport code統合                       |
| **Real-time control simulation** | Controller + plasma responsモデル              |
| **AC loss estimation**           | Long pulse scenario全体のAC損失評価            |
| **Disruption mitigation**        | Fast shutdown with ECCD contributionモデリング |

### 8.3 運転戦略推奨

#### 8.3.1 Commissioning Phase

**Phase 1: Non-nuclear operation**

1. Wall conditioning（ECRH discharge cleaning）
2. Plasma initiation（ECRH assisted start-up検証）
3. L-mode operation（magnetics control検証）
4. H-mode transition（ECH単独、then with NBI）
5. Current ramp optimization（Ejima係数測定）

**Phase 2: Low-power operation**
6. Kinetics control commissioning
7. Divertor detachment control
8. Density limit exploration
9. MHD control（tearing mode, ELM）

#### 8.3.2 Burning Plasma Phase

**Reference Scenario運転**:

1. ECRH assisted start-up（3 MW, <3 ms breakdown）
2. Current ramp-up（最適化波形、Ejima~0.45）
3. H-mode transition（auxiliary power制御）
4. Density ramp（pellet + gas, toward ignition）
5. Burn control（density feedback, Te監視、）
6. Safe termination（controlled ramp-down）

**Advanced Scenario開発**:

1. Reverse shear q-profile生成（early ECCD + ramp control）
2. ITB形成（協調magnetic + kinetic control）
3. Steady-state operation（high bootstrap fraction）
4. βN optimization（resistive wall mode control）

### 8.4 診断要求（ECCD/制御用）

#### 8.4.1 ECCD診断

| 診断                   | 目的                            | 要求精度   |
| ---------------------- | ------------------------------- | ---------- |
| **ECE**                | Te profile, absorption location | Δr < 5 cm  |
| **Thomson scattering** | Te, ne profile                  | Δr < 10 cm |
| **MSE**                | Current profile j(r)            | Δj/j < 10% |
| **Polarimetry**        | Current profile (alternative)   | -          |
| **Hard X-ray**         | Fast electron tail              | -          |

#### 8.4.2 制御診断（Real-time）

| 診断                  | 目的                  | 要求時間分解能 |
| --------------------- | --------------------- | -------------- |
| **Magnetics**         | Position, shape       | < 1 ms         |
| **Interferometry**    | Line-averaged density | < 10 ms        |
| **Bolometry**         | Radiated power        | < 10 ms        |
| **Divertor Langmuir** | Edge/divertor Te, ne  | < 10 ms        |
| **Neutron counter**   | Fusion power (DT)     | < 100 ms       |
| **IR camera**         | Surface temperature   | < 10 ms        |

---

## 9. 結論

### 9.1 Chapter 8の主要成果

**Chapter 8: Plasma operation and control** は、以下を包括的にカバー：

1. **Wall conditioning**: RF discharge cleaning含む各種手法
2. **Magnetic control**: 超伝導コイル制約下での形状・位置制御
3. **Kinetics control**: 3-power制御戦略
4. **Plasma initiation**: ECRH assisted start-up（3 MW, 0.3 V/m誘導電場）
5. **Current ramp-up/down**: Ejima式に基づく最適化
6. **Advanced tokamak control**: ITB生成、定常運転制御

### 9.2 ECCDの役割

ITERにおけるECCD/ECRHの主要役割は多岐にわたる：

**主要機能**:

1. **Central heating**: H-mode accessと核融合点火
2. **Start-up assist**: Reliable breakdown（3 MW, 90-140 GHz）
3. **Current drive**: On-axis（中心q制御）、off-axis（プロファイル制御）
4. **MHD stabilization**: Neoclassical tearing mode, sawtooth制御
5. **ELM control**: 周波数制御（Type I実証）

**unique advantages**:

- 高度に局所化された加熱・電流駆動
- 真空伝搬（launcher位置の自由度）
- 周波数・入射角制御による吸収位置制御
- Real-time steering可能

### 9.3 実装feasibility

**技術的成熟度**:

- 物理理論: ★★★★★（非常に高い）
- 実験実証: ★★★★☆（ほぼ十分、一部要追加実証）
- 技術開発: ★★★☆☆（開発進行中、1 MW gyrotronが鍵）
- システム統合: ★★★☆☆（設計段階、実証必要）

**Critical path items**:

1. 170 GHz, 1 MW, SS gyrotron開発
2. ダイヤモンドウィンドウ技術
3. Off-axis ECCD実証（medium size tokamak）
4. 統合制御アルゴリズム開発

### 9.4 ITER Physics Basisの貢献

1999年のITER Physics Basisは、ITERの物理設計の強固な基盤を提供：

- 包括的な物理データベース
- 実験的に検証されたスケーリング則
- 詳細なシミュレーションツール
- 明確な技術開発課題の同定

**ECCD/ECRH関連では**:

- 定量的効率予測（実験と理論の一致）
- 複数の適用シナリオの実証
- 技術的feasibilityの評価
- 制御戦略の具体化

---

## 10. 参考文献

主要参考文献（ITER Physics Basis該当章）:

1. **Chapter 6**: ITER Physics Expert Group on Energetic Particles, Heating and Current Drive, et al., "Chapter 6: Plasma auxiliary heating and current drive", Nuclear Fusion **39**, 2495-2539 (1999)

2. **Chapter 8**: ITER Physics Expert Group on Disruptions, Plasma Control, and MHD, et al., "Chapter 8: Plasma operation and control", Nuclear Fusion **39**, 2577-2638 (1999)

---

## Appendix A: 略語・用語集

| 略語 | 正式名称                                | 日本語                       |
| ---- | --------------------------------------- | ---------------------------- |
| ECCD | Electron Cyclotron Current Drive        | 電子サイクロトロン電流駆動   |
| ECRH | Electron Cyclotron Resonance Heating    | 電子サイクロトロン共鳴加熱   |
| ECH  | Electron Cyclotron Heating              | 電子サイクロトロン加熱       |
| ECRF | Electron Cyclotron Range of Frequencies | 電子サイクロトロン周波数帯   |
| ICRF | Ion Cyclotron Range of Frequencies      | イオンサイクロトロン周波数帯 |
| LHCD | Lower Hybrid Current Drive              | 低域混成波電流駆動           |
| NBI  | Neutral Beam Injection                  | 中性粒子入射                 |
| ITB  | Internal Transport Barrier              | 内部輸送障壁                 |
| ELM  | Edge Localized Mode                     | エッジ局在モード             |
| MHD  | Magnetohydrodynamics                    | 磁気流体力学                 |
| PF   | Poloidal Field                          | ポロイダル磁場               |
| TF   | Toroidal Field                          | トロイダル磁場               |
| SOF  | Start of Flat-top                       | フラットトップ開始           |
| SOB  | Start of Burn                           | 燃焼開始                     |
| EOB  | End of Burn                             | 燃焼終了                     |
| LFS  | Low Field Side                          | 低磁場側                     |
| HFS  | High Field Side                         | 高磁場側                     |
| βN   | Normalized beta                         | 規格化ベータ値               |

---

**レポート作成日**: 2026年3月2日  
**作成者**: AI分析システム  
**データソース**: ITER Physics Basis (1999), Nuclear Fusion Vol. 39
