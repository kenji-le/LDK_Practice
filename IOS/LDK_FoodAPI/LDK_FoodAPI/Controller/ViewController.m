//
//  ViewController.m
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

@synthesize collectionRecipes;

# pragma mark - Lifecycle

- (void)viewDidLoad {
    [super viewDidLoad];
    [self getData];
}

# pragma mark - Methods

- (void)getData {
    [CONTENT_MANAGER getFoodListWithCompletion:^(BOOL success, NSArray *recipes, NSString *errorMessage) {
        if (success) {
            NSLog(@"SUCCESS count=%lu", (unsigned long)recipes.count);
            self->recipeList = [[NSArray alloc] initWithArray:recipes];
            [self setupView];
        } else {
            NSLog(@"FAILED errorMessage=%@", errorMessage);
            UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Error" message:errorMessage preferredStyle:UIAlertControllerStyleAlert];
            
            UIAlertAction *actionOK = [UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault handler:nil];
            
            [alert addAction:actionOK];
            [self presentViewController:alert animated:YES completion:nil];
        }
    }];
}

- (void)setupView {
    [self setTitle:@"Food List"];
    [collectionRecipes setFrame:CGRectMake(0, STATUS_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - STATUS_HEIGHT)];
    [collectionRecipes registerNib:[UINib nibWithNibName:@"RecipeCollectionViewCell" bundle:nil] forCellWithReuseIdentifier:CELL_IDENTIFIER];
    collectionRecipes.delegate = self;
    collectionRecipes.dataSource = self;
    [collectionRecipes reloadData];
    //    self.automaticallyAdjustsScrollViewInsets = NO;
}

# pragma mark - Collection View's delegate & datasource

- (nonnull __kindof UICollectionViewCell *)collectionView:(nonnull UICollectionView *)collectionView cellForItemAtIndexPath:(nonnull NSIndexPath *)indexPath {
    RecipeCollectionViewCell *cell = [collectionRecipes dequeueReusableCellWithReuseIdentifier:CELL_IDENTIFIER forIndexPath:indexPath];
    Recipe *recipe = [recipeList objectAtIndex:indexPath.row];
    [cell setCellWithRecipe:recipe];
    return cell;
}

- (NSInteger)collectionView:(nonnull UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section {
    return recipeList.count;
}

- (CGSize)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout sizeForItemAtIndexPath:(NSIndexPath *)indexPath {
    int column = 2;
    float width = (SCREEN_WIDTH - MARGIN*(column+1))/column;
    return CGSizeMake(width, width);
}

- (NSInteger)numberOfSectionsInCollectionView:(UICollectionView *)collectionView {
    return 1;
}

- (UIEdgeInsets)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout insetForSectionAtIndex:(NSInteger)section {
    return UIEdgeInsetsMake(MARGIN, MARGIN, MARGIN, MARGIN);
}

- (CGFloat)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout minimumLineSpacingForSectionAtIndex:(NSInteger)section {
    return MARGIN;
}

- (CGFloat)collectionView:(UICollectionView *)collectionView layout:(UICollectionViewLayout *)collectionViewLayout minimumInteritemSpacingForSectionAtIndex:(NSInteger)section {
    return MARGIN;
}

- (void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath{
    FoodViewController *foodView = [[FoodViewController alloc] init];
    foodView.recipe = [recipeList objectAtIndex:indexPath.row];
    [self.navigationController pushViewController:foodView animated:YES];
}

@end
